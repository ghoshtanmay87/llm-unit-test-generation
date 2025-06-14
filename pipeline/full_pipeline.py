import logging
from langgraph.graph import StateGraph, END
from config.pipeline_state import PipelineState
from agents.coverage_agent import TestCoverageAgent
from agents.refinement_agent import TestRefinementAgent
from agents.regeneration_agent import UserStoryRegenerationAgent
from agents.story_generation_agent import UserStoryGenerationAgent
from agents.test_execution_agent import CodeExecutionAgent
from agents.test_generation_agent import UnitTestGenerationAgent
from agents.validation_agent import UserStoryValidationAgent
from pipeline.base_pipeline import BasePipeline


class FullPipeline(BasePipeline):
    def __init__(self, llm=None, config=None):
        super().__init__(llm, config)

    def build_graph(self):
        workflow = StateGraph(PipelineState)
        workflow.add_node("generate_user_stories_agent", UserStoryGenerationAgent(self.llm, self.config))
        workflow.add_node("validate_user_stories_agent", UserStoryValidationAgent(self.config))
        workflow.add_node("regenerate_user_stories_agent", UserStoryRegenerationAgent(self.llm, self.config))
        workflow.add_node("unit_test_generation_agent", UnitTestGenerationAgent(self.llm, self.config))
        workflow.add_node("code_execution_agent", CodeExecutionAgent(self.config))
        workflow.add_node("test_refinement_agent", TestRefinementAgent(self.llm, self.config))
        workflow.add_node("test_coverage_agent", TestCoverageAgent(self.config))

        workflow.set_entry_point("generate_user_stories_agent")

        workflow.add_edge("generate_user_stories_agent", "validate_user_stories_agent")
        workflow.add_conditional_edges(
            "validate_user_stories_agent",
            self.check_story_validation,
            {
                "success": "unit_test_generation_agent",    
                "invalid_stories": "regenerate_user_stories_agent",
                "fail_no_valid_stories": END
            }
        )
        workflow.add_edge("regenerate_user_stories_agent", "validate_user_stories_agent")
        workflow.add_edge("unit_test_generation_agent", "code_execution_agent")
        workflow.add_conditional_edges(
            "code_execution_agent",
            self.check_status, 
            {
                "retry": "test_refinement_agent", # Test failed
                "pass": "test_coverage_agent", # Test passed
                "max_retries_reached": END # Exit after too many retries
            }
        )
        workflow.add_edge("test_refinement_agent", "code_execution_agent")
        workflow.add_edge("test_coverage_agent", END)
        return workflow.compile()

    def check_story_validation(self, state: PipelineState):
        if state.status == "fail_no_valid_stories":
            return "fail_no_valid_stories"
        return "success" if not state.has_story_errors else "invalid_stories"
    
    def check_status(self, state: PipelineState):
        return state.status