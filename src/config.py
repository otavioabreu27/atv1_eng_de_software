import json

class Config:
    def __init__(self, config: dict):
        self.host=config["db"]["host"]
        self.user=config["db"]["user"]
        self.password=config["db"]["password"]
        self.db=config["db"]["db"]

f = open("config.json")
config_file = json.load(f)

config = Config(config_file)