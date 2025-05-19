"""Набор классов для представления электромобилей."""

from car import Car


class Battery():
	"""Простая модель аккамулятора"""

	def __init__(self,battery_size = 75):
		"""Инициализирует атрибуты аккумулятора."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Выводит информацию о мощности аккамулятора."""
		print(f"This car has a {self.battery_size} - kWh battery.")

	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		"""
		Проверяет размер аккамулятора и ставит мощность 100,
		если она имеет другое значение.
		"""
		if not self.battery_size == 100:
			self.battery_size = 100


class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электромобилей."""

	def __init__(self, make, model, year):
		"""
		Инициализирует атрибуты класса родителя.
		Затем инициализируем атрибуты, специфические для электромобилей.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()