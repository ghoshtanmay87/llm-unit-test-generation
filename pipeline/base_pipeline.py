import logging
from langgraph.graph import StateGraph, END
from IPython.display import display, Image
from llm.llm_factory import LLMFactory
from config.config import Config
from config.pipeline_state import PipelineState
from agents.coverage_agent import TestCoverageAgent
from agents.story_generation_agent import UserStoryGenerationAgent
from agents.test_generation_agent import UnitTestGenerationAgent


class BasePipeline:
    def __init__(self, llm=None, config=None):
        self.config = config or Config("config/pipeline_config.json", "config/global_config.json")
        self.llm = llm or LLMFactory(self.config).initialise()
        self.graph = self.build_graph()
    
    def build_graph(self):
        workflow = StateGraph(PipelineState)
        workflow.add_node("generate_user_stories_agent", UserStoryGenerationAgent(self.llm, self.config))
        workflow.add_node("unit_test_generation_agent", UnitTestGenerationAgent(self.llm, self.config))
        workflow.add_node("test_coverage_agent", TestCoverageAgent(self.config))

        workflow.set_entry_point("generate_user_stories_agent")

        workflow.add_edge("generate_user_stories_agent", "unit_test_generation_agent")
        workflow.add_edge("unit_test_generation_agent", "test_coverage_agent")
        workflow.add_edge("test_coverage_agent", END)
        return workflow.compile()

    def run(self, function_code: str):
        initial_state = PipelineState(function_code=self.clean_code(function_code), retry_count=0, story_retry_count=0)
        final_state = self.graph.invoke(initial_state)
        display(Image(self.graph.get_graph(xray=True).draw_mermaid_png()))
        logging.info("----- END -----")
        return final_state
    
    def clean_code(self, function_code: str):
        # Handle line breaks inside string literals and normalize escape characters
        function_code = function_code.replace("\\n", "\\\\n").replace("\\t", "\\\\t").replace("\\r", "\\\\r")
        return function_code.encode().decode('unicode_escape')
