import json
import os


class BuildingData:
    def __init__(self, path="assets/data/buildings.json"):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Building data file not found: {path}")

        with open(path, "r", encoding="utf-8") as file:
            self._data = json.load(file)

        self._validate_data()

    def get(self, building_type):
        """Получить словарь параметров постройки по типу."""
        data = self._data.get(building_type)
        if data is None:
            raise ValueError(f"Unknown building type: {building_type}")
        return data

    def all_types(self):
        """Список всех доступных типов построек."""
        return list(self._data.keys())

    def is_passable(self, building_type):
        """Проверить, проходима ли постройка."""
        return self.get(building_type).get("passable", True)

    def _validate_data(self):
        """Проверка на наличие ключевых полей."""
        for name, data in self._data.items():
            if "passable" not in data:
                print(f"[WARNING] '{name}' has no 'passable' field! Defaulting to True.")
