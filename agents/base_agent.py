import re
import json
import ast
from pathlib import Path
from config.config import Config
import logging
import json


class BaseAgent:
    def __init__(self, config: Config):
        self.config = config

    def extract_json_from_response(self, text: str):
        # Remove backticks and json tag
        match = re.search(r"```(?:json|python)?\s*([\s\S]*?)\s*```", text)
        if match:
            data = match.group(1).strip()
            # Remove leading assignments`
            assign_match = re.match(r"^[\w_]+\s*=\s*(\[|\{)", data)
            if assign_match:
                eq_index = data.find("=")
                data = data[eq_index + 1:].strip()
            return data

        return text.strip()
    
    def get_response(self, response):
        match self.config.selected_model_index:
            case 1 | 2:
                return response.content
            case _:
                response

    def extract_function_name(self, function_code: str):
        match = re.search(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", function_code)
        return match.group(1) if match else None
    
    def find_top_level_function_name(self, function_code: str):
        # Parses the code to find the top level function, which is not called by others
        tree = ast.parse(function_code)
        all_funcs = set()
        called_funcs = set()

        class FuncVisitor(ast.NodeVisitor):
            def visit_FunctionDef(self, node):
                if not isinstance(getattr(node, 'parent', None), ast.ClassDef):
                    all_funcs.add(node.name)
                    for subnode in ast.walk(node):
                        if isinstance(subnode, ast.Call) and isinstance(subnode.func, ast.Name):
                            called_funcs.add(subnode.func.id)

            def visit_ClassDef(self, node):
                for child in node.body:
                    if isinstance(child, ast.FunctionDef):
                        child.parent = node

        FuncVisitor().visit(tree)
        
        if(len(all_funcs) == 1):
            return next(iter(all_funcs), None)
        
        entry_funcs = all_funcs - called_funcs
        logging.info(f"[BaseAgent] entry_function: {entry_funcs}")
        return next(iter(entry_funcs), None)
    
    def extract_code_from_output(self, agent_output: str):
        code_blocks = re.findall(r"```(?:python)?\s*([\s\S]+?)```", agent_output)
        if code_blocks:
            return "\n\n".join(block.strip() for block in code_blocks)
        else:
            # return everything if code block not found
            return ""
        
    def clean_for_python_parsing(self, raw_text: str):
        # Fix number formats
        raw_text = re.sub(r'(?<=\d),(?=\d)', '', raw_text)
        return raw_text.replace("null", "None").replace("true", "True").replace("false", "False")
        
    def load_prompt(self, path: str, **kwargs):
        template = Path(path).read_text()
        return template.format(**kwargs)
    
    def normalize_input(self, input: str):
        return json.dumps(input, sort_keys=True)