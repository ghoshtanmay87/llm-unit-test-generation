from dataclasses import dataclass, field


@dataclass
class PipelineState:
    function_code: str = None
    user_stories: list = field(default_factory=list)
    unit_tests: str = None
    story_retry_count: int = 0
    retry_count: int = 0
    status: str = "pass"
    has_story_errors: bool = False
    user_story_validation_errors: list = field(default_factory=list)
    test_result_stderr: str = None
    test_file_name: str = None
    coverage_percent: float = 0.0