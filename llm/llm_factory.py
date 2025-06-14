import os
from langchain_openai import ChatOpenAI


class LLMFactory:
    def __init__(self, config):
        self.config = config

    def initialise(self):
        model_index = self.config.selected_model_index

        match model_index:
            case 1:
                self.set_openai_api_key()
                return ChatOpenAI(model=self.config.models_list[model_index], temperature=self.config.model_temperature)
            case 2:
                self.set_deepseek_api_key()
                return ChatOpenAI(model=self.config.models_list[model_index], temperature=self.config.model_temperature, base_url="https://api.deepseek.com")
            case _:
                self.set_openai_api_key()
                return ChatOpenAI(model=self.config.models_list[1], temperature=self.config.model_temperature)

    def set_openai_api_key(self):
        os.environ["OPENAI_API_KEY"] = self.config.open_ai_api_key
    
    def set_deepseek_api_key(self):
        os.environ["OPENAI_API_KEY"] = self.config.deepseek_api_key