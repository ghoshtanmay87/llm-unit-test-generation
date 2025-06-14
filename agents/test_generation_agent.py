import logging
import re
from langchain_core.messages import HumanMessage
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState


class UnitTestGenerationAgent(BaseAgent):
    def __init__(self, llm, config: Config):
        super().__init__(config)
        self.llm = llm
        self.config = config

    def __call__(self, state: PipelineState):
        message = HumanMessage(
            content=self.load_prompt(
                "prompts/unit_test_gen.txt", 
                user_stories=state.user_stories, 
                function_code=state.function_code)
        )
        response = self.llm.invoke([message])
        unit_tests = self.extract_code_from_output(self.get_response(response))
        function_name = self.extract_function_name(state.function_code)
        state.unit_tests = self.clean_test_code_for_execution(unit_tests, function_name)

        logging.info(f"[UnitTestGenerationAgent] Generated Unit Tests")
        return state
    
    def clean_test_code_for_execution(self, test_code: str, function_name: str):
        cleaned = re.sub(
            rf"from\s+your_module\s+import\s+{function_name}.*\n",
            "",
            test_code
        )
        return cleaned