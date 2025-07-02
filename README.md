# A Multi-Agent Framework for LLM Based Reliable Unit Test Generation

 A modular, retry aware, optional feedback enabled unit test generation pipeline using Large Language Models (LLMs). It implements a modular architecture with LangGraph, enabling structured user story generation, user story validation, user story regeneration, unit test test synthesis, test execution, refinement and coverage analysis.

---

## Setup (Mac)

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Update configuration**  
   Update following configurations in `global_config.json` inside `config/`:

   ```json
    {
      "selected_model_index": 1,
      "open_ai_api_key": "<openai-api-key>",
      "deepseek_api_key": "<deepseek-api-key>"
    }
   ```

---

## Running the Pipelines

- **Baseline**  
  notebook: `baseline.ipynb`

- **Full Pipeline**  
  notebook: `pipeline.ipynb`

Before running the pipeline, update the `start` and `limit` parameters while running `run_pipeline()` to control how many tasks from the dataset are to be processed:

- `start`: The index (1-based) of the first task to process from the dataset.
- `limit`: The number of tasks to process starting from `start`.

Example: To run 5 tasks starting from the 100th task, set `start=100` and `limit=5`.

```python
run_pipeline(jsonl_path="datasets/mbpp.jsonl", pipeline=pipeline, log_dir="logs", function_key="code", log_prefix="mbpp-baseline", start=100, limit=5)
```
