from langchain_core.messages import HumanMessage
import logging
import ast
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState


class UserStoryRegenerationAgent(BaseAgent):
    def __init__(self, llm, config: Config):
        super().__init__(config)
        self.llm = llm
        self.config = config

    def __call__(self, state: PipelineState):
        entry_func = self.find_top_level_function_name(state.function_code)
        message = HumanMessage(content=self.load_prompt(
            "prompts/user_story_regen.txt",
            entry_func=entry_func,
            function_code=state.function_code,
            user_story_validation_errors=state.user_story_validation_errors))

        response = self.llm.invoke([message])
        response_text = self.get_response(response)
        logging.info(f"[UserStoryRegenerationAgent] response from LLM: {response_text}")
        
        try:
            raw_json = self.clean_for_python_parsing(self.extract_json_from_response(response_text))
            corrected = ast.literal_eval(raw_json)
                
        except Exception as e:
            logging.info(f"[UserStoryRegenerationAgent] parse error: {e} for raw_json: {raw_json}")
            corrected = []

        # Replace invalid stories with corrected ones
        logging.info(f"[UserStoryRegenerationAgent] failed_stories: {state.user_story_validation_errors}")
        invalid_inputs = {self.normalize_input(s["input"]) for s in state.user_story_validation_errors}
        new_stories = [s for s in state.user_stories if self.normalize_input(s["input"]) not in invalid_inputs]
        new_stories.extend(corrected)
        state.user_stories = new_stories
        logging.info(f"[UserStoryRegenerationAgent] Corrected invalid stories: {new_stories}")
        state.story_retry_count = state.story_retry_count + 1
        return state