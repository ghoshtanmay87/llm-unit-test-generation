# utils/pipeline_runner.py

import json
import logging
from config.logger import setup_logging

def run_pipeline(jsonl_path, pipeline, log_dir, function_key="code", task_ids=None, start=1, limit=None, log_prefix=None):
    log_path = setup_logging(prefix=log_prefix, log_dir=log_dir)
    logging.info(f"Logging to: {log_path}")

    success_count = 0
    failure_count = 0
    results = []
    task_ids_set = set(task_ids) if task_ids else None

    with open(jsonl_path, 'r') as file:
        for idx, line in enumerate(file, start=1):
            try:
                data = json.loads(line)
                task_id = data.get("task_id")

                if task_ids_set and task_id not in task_ids_set:
                    continue
                if not task_ids_set and idx < start:
                    continue
                if not task_ids_set and limit and idx >= start + limit:
                    break

                function_code = data.get(function_key)
                coverage = 0.0

                logging.info(f"Running Task ID: {task_id}")
                result = pipeline.run(function_code)
                logging.info(f"Completed Task ID: {task_id}\n")

                test_cases = result.get("unit_tests")
                status = result.get("status")
                coverage = result.get("coverage_percent")
                retry_count = result.get("story_retry_count", 0)

                if not test_cases or status in ["max_retries_reached", "fail_no_valid_stories"]:
                    failure_count += 1
                    results.append({
                        "task_id": task_id,
                        "success": False,
                        "error": f"Pipeline ended with status: {status or 'no test cases generated'}",
                        "retry": retry_count,
                        "coverage": coverage
                    })
                else:
                    success_count += 1
                    results.append({
                        "task_id": task_id,
                        "success": True,
                        "result": f"{len(result['user_stories'])} tests generated",
                        "retry": retry_count,
                        "coverage": coverage
                    })

            except Exception as e:
                failure_count += 1
                results.append({
                    "task_id": task_id or idx,
                    "success": False,
                    "error": str(e),
                    "retry": retry_count if 'result' in locals() else 0,
                    "coverage": coverage
                })

    logging.info("\nSummary:")
    logging.info(f"Successes: {success_count}")
    logging.info(f"Failures: {failure_count}")
    logging.info(f"Total Processed: {success_count + failure_count}")
    logging.info(f"*** Results: {results}")
    return results