class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item, amount=1):
        """Добавить предмет в инвентарь"""
        self.items[item] = self.items.get(item, 0) + amount

    def remove(self, item, amount=1):
        """Удалить предмет (если достаточно)"""
        if self.items.get(item, 0) >= amount:
            self.items[item] -= amount
            if self.items[item] <= 0:
                del self.items[item]
            return True
        return False

    def has(self, item, amount=1):
        """Проверить, есть ли нужное количество"""
        return self.items.get(item, 0) >= amount

    def get(self, item):
        """Сколько предмета"""
        return self.items.get(item, 0)

    def all_items(self):
        """Все предметы"""
        return self.items.items()
