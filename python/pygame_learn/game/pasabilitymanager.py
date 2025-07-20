class PassabilityManager:
    def __init__(self, map_objects):
        """
        map_objects — список объектов на карте (ресурсы, здания, стены и т.п.)
        Каждый объект должен иметь атрибуты: rect и passable (bool)
        """
        self.map_objects = map_objects

    def is_position_passable(self, rect):
        """
        Проверяет, можно ли пройти в данную позицию (rect)
        """
        for obj in self.map_objects:
            if obj.rect.colliderect(rect) and not obj.passable:
                return False
        return True
