import os
import subprocess
import logging
from agents.base_agent import BaseAgent
from config.config import Config
from config.pipeline_state import PipelineState


class TestCoverageAgent(BaseAgent):
    def __init__(self, config: Config):
        super().__init__(config)
        self.config = config

    def __call__(self, state: PipelineState):
        test_file = state.test_file_name
        if not test_file:
            function_name = self.find_top_level_function_name(state.function_code)
            test_file = self.config.test_file.format(function_name=function_name)
            if os.path.exists(test_file):
                os.remove(test_file)
                print(f"Existing file '{test_file}' deleted.")
            
            with open(test_file, "w") as file:
                state.full_test_script = f"{state.function_code.strip()}\n\n{state.unit_tests}"
                file.write(state.full_test_script)

        module_name = os.path.splitext(os.path.basename(test_file))[0]

        try:
            logging.info(f"[TestCoverageAgent] Running pytest with coverage for {test_file}")
            result = subprocess.run([
                "pytest",
                test_file,
                f"--cov={module_name}",
                "--cov-report=term",
                "--color=no"
            ], capture_output=True, text=True)

            stdout = result.stdout
            stderr = result.stderr
            logging.info(f"[TestCoverageAgent] Pytest Coverage Output: {stdout} & {stderr}")
            for line in stdout.splitlines():
                if "TOTAL" in line and "%" in line:
                    coverage_str = line.split()[-1].strip("%")
                    state.coverage_percent = float(coverage_str)
                    break
            else:
                state.coverage_percent = 0.0
                logging.warning("[TestCoverageAgent] Could not extract coverage percent.")

        except Exception as e:
            logging.error(f"[TestCoverageAgent] Failed to measure coverage: {e}")
            state.coverage_percent = 0.0

        return state