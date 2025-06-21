from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000):
        """Иницилизирует атрибуты блУждания."""
        self.num_points = num_points
        # Все блуждания начинаются с точки(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            x_step=self.get_step_x()
            y_step=self.get_step_y()
            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step_x(self):
        """Вычисляет шаг по y."""
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance
        return x_step


    def get_step_y(self):
        """Вычисляет шаг по x."""
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance
        return y_step