import json
import importlib

class Config:
    def __init__(self, *config_paths):
        config_data = {}
        for path in config_paths:
            with open(path, "r") as f:
                data = json.load(f)
                config_data.update(data)

        for key, value in config_data.items():
            setattr(self, key, value)

        self.models_list = {int(k): v for k, v in self.models_list.items()}
        self.global_env = {name: importlib.import_module(name) for name in self.global_env}