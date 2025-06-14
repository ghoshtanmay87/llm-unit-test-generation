from langchain_core.messages import HumanMessage
import logging
import ast
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState


class UserStoryGenerationAgent(BaseAgent):
    def __init__(self, llm, config: Config):
        super().__init__(config)
        self.llm = llm
        self.config = config

    def __call__(self, state: PipelineState):
        entry_func = self.find_top_level_function_name(state.function_code)
        logging.info(f"[UserStoryGenerationAgent] processing entry function named {entry_func} with function code: {state.function_code}")
        message = HumanMessage(
            content = self.load_prompt(
                "prompts/user_story_gen_cot.txt", 
                entry_func=entry_func, 
                function_code=state.function_code)
        )
        response = self.llm.invoke([message])
        
        try:
            response = self.get_response(response)
            logging.info(f"[UserStoryGenerationAgent] LLM Response: {response}")
            raw_json = self.clean_for_python_parsing(self.extract_json_from_response(response))
            stories_json = ast.literal_eval(raw_json)
            state.user_stories = stories_json
        except Exception as e:
            logging.info(f"[UserStoryGenerationAgent] parsing failed: {e}")
            raise

        logging.info(f"[UserStoryGenerationAgent] user_stories: {state.user_stories}")
        return state