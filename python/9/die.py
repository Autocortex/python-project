from random import randint

class Die():
	"""Простая модель бросания кубиков."""

	def __init__(self, sides = 6):
		"""Инициализирует атрибут sides."""
		self.sides = sides

	def roll_die(self):
		"""Имитирует бросание кубиков и выводит результат."""
		print(randint(1, self.sides))


my_sides = Die(10)
my_sides.roll_die()

my_sides = Die(20)
my_sides.roll_die()

