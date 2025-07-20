class Employee():
	"""Описывает работника."""

	def __init__(self, first_name, last_name, money):
		""""Инизциализирует атрибуты first_name, last_name, money."""
		self.first_name = first_name
		self.last_name = last_name
		self.money = money

	def give_raise(self, amount = 5000):
		"""Увеличивает ежегодный оклад."""
		self.money += amount
		return self.money


