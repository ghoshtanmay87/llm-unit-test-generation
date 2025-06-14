import logging
import textwrap
import inspect
import signal
from langchain_core.messages import HumanMessage
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState


class UserStoryValidationAgent(BaseAgent):
    def __init__(self, config: Config):
        super().__init__(config)
        self.config = config

    def __call__(self, state: PipelineState):
        if not state.user_stories:
            logging.info("[UserStoryValidationAgent] No user stories available. Cannot continue.")
            state.status = "fail_no_valid_stories"
            return state

        errors = self.validate_user_stories(state.function_code, state.user_stories)

        if errors:
            state.has_story_errors = True
            state.user_story_validation_errors = errors
            logging.info(f"[UserStoryValidationAgent] Errors found in user stories: {errors}")

            # Retry logic
            if state.story_retry_count >= self.config.max_tries:
                logging.info(f"[UserStoryValidationAgent] Max story retries reached. Discarding invalid stories.")
                invalid_inputs = {self.normalize_input(e["input"]) for e in errors}
                valid_stories = [s for s in state.user_stories if self.normalize_input(s["input"]) not in invalid_inputs]
                
                if valid_stories:
                    logging.info(f"[UserStoryValidationAgent] Proceeding with {len(valid_stories)} valid stories.")
                    state.user_stories = valid_stories
                    state.has_story_errors = False
                else:
                    logging.info(f"[UserStoryValidationAgent] No valid stories left. Cannot continue.")
                    state.status = "fail_no_valid_stories"
        else:
            state.has_story_errors = False
            logging.info("[UserStoryValidationAgent] All user stories validated.")

        return state
    
    def validate_user_stories(self, function_code: str, user_stories: list):
        errors = []
        try:
            exec(textwrap.dedent(function_code), self.config.global_env)
        except Exception as e:
            return [{"error": f"Failed to parse function: {str(e)}"}]

        func_name = self.find_top_level_function_name(function_code)
        if not func_name:
            func_name = next((k for k in self.config.global_env if callable(self.config.global_env[k])), None)

        func = self.config.global_env[func_name]
        for story in user_stories:
            # logging.info(f"[UserStoryValidationAgent] got story: {story}")
            test_input = story.get("input")
            expected = story.get("expected_output")

            try:
                # Handle different input types dynamically
                signal.signal(signal.SIGALRM, self.timeout_handler)
                signal.alarm(5)
                result = self.invoke(func, test_input)
                signal.alarm(0)
                expected_repr = repr(expected) if not isinstance(expected, str) else expected
                result_repr = repr(result) if not isinstance(result, str) else result

                if result_repr != expected_repr and expected != result:
                    errors.append({
                        "scenario": story.get("scenario"),
                        "input": test_input,
                        # "expected_output": expected, # uncomment to enable expected output feedback to model
                        "error": "Function output did not match expected_output",
                        "actual_output": result,
                        "reasoning": story.get("reasoning")
                    })

            except TimeoutError:
                logging.error("[UserStoryValidationAgent] TimeoutError: test execution exceeded time limit")
                errors.append({
                    "scenario": story.get("scenario"),
                    "input": test_input,
                    "error": "Timeout during execution",
                    "expected_output": expected
                })
            except Exception as e:
                errors.append({
                    "scenario": story.get("scenario"),
                    "input": test_input,
                    "error": str(e),
                    "expected_output": expected
                })

        return errors

    def invoke(self, func, test_input):
        sig = inspect.signature(func)
        param_count = len(sig.parameters)

        try:
            if isinstance(test_input, dict):
                return func(**test_input)
            elif isinstance(test_input, (list, tuple)):
                if param_count == 1:
                    return func(test_input)
                else:
                    return func(*test_input)
            else:
                return func(test_input)
        except TypeError as e:
            logging.error(f"[UserStoryValidationAgent] TypeError: {e}")
            raise

    @staticmethod
    def timeout_handler(signum, frame):
        raise TimeoutError(f"Function execution exceeded timeout.")