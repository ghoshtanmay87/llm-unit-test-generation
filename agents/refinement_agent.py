from langchain_core.messages import HumanMessage
import logging
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState

class TestRefinementAgent(BaseAgent):
    def __init__(self, llm, config: Config):
        super().__init__(config)
        self.llm = llm
        self.config = config

    def __call__(self, state: PipelineState):
        message = HumanMessage(
            content=self.load_prompt(
                "prompts/unit_test_refinement.txt",
                test_result_stderr=state.test_result_stderr, 
                function_code=state.function_code,
                unit_tests=state.unit_tests)
        )
        logging.info(f"[TestRefinementAgent] Got test execution errors")
        response = self.llm.invoke([message])
        updated_test = self.extract_code_from_output(self.get_response(response))
        if updated_test.strip():
            state.unit_tests = self.extract_code_from_output(self.get_response(response))
            logging.info("[TestRefinementAgent] Refined test cases.")
        else:
            logging.warning(f"[TestRefinementAgent] LLM failed to return valid test code on retry {state.retry_count + 1}. Keeping previous test.")

        state.retry_count = state.retry_count + 1
        return state