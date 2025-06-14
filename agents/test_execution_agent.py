import os
import logging
import subprocess
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState


class CodeExecutionAgent(BaseAgent):
    def __init__(self, config: Config):
        self.config = config

    def __call__(self, state: PipelineState):
        logging.info("[CodeExecutionAgent] starting execution")
        function_name = self.find_top_level_function_name(state.function_code)
        test_file_name = self.config.test_file.format(function_name=function_name)
        state.test_file_name = test_file_name
        if os.path.exists(test_file_name):
            os.remove(test_file_name)
            print(f"Existing file '{test_file_name}' deleted.")

        with open(test_file_name, "w") as file:
            full_test_script = f"{state.function_code.strip()}\n\n{state.unit_tests}"
            file.write(full_test_script)

        # Run pytest on the generated test file
        result = subprocess.run(["pytest", test_file_name, "--color=no"], capture_output=True, text=True)
        test_output = (result.stdout + result.stderr).lower()
        if "failed" in test_output:
            if state.retry_count >= self.config.max_tries:
                logging.info("[CodeExecutionAgent] Max retries reached. Ending.")
                state.status = "max_retries_reached"
            else:
                logging.info("[CodeExecutionAgent] Test failed. Triggering retry.")
                state.test_result_stderr = test_output
                state.status = "retry"
        else:
            logging.info("[CodeExecutionAgent] Tests passed. Exiting.")
            state.status = "pass"
            logging.info(f"[CodeExecutionAgent] result.stdout: {result.stdout}")

        return state