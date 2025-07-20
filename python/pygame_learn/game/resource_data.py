import json
import os

class ResourceData:
    def __init__(self, json_path="assets/data/resources.json"):
        with open(json_path, "r", encoding="utf-8") as file:
            self._data = json.load(file)

    def get(self, resource_type):
        return self._data.get(resource_type)

    def all_types(self):
        return list(self._data.keys())

    def random_type(self):
        import random
        return random.choice(self.all_types())
