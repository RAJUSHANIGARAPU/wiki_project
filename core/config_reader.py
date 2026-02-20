import json
import os


class ConfigReader:
    def __init__(self, env="qas"):
        base_path = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(base_path, "config", "environments.json")

        with open(config_path) as f:
            self.config = json.load(f)[env]

    def get_base_url(self):
        return self.config["base_url"]
