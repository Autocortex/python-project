import unittest
from car import Car

class TestCar(unittest.TestCase):
	"""Тестируем на ошибки клас Car."""

	def setUp(self):
		"""Инициируем атрибуты класса Car."""
		self.car = Car('BMV','S5', 25)

	def test_default_odometer(self):
		"""Проверка значения одометра по умолчанию."""
		self.assertEqual(25, self.car.odometer_reading)

	def test_update_odometer(self):
		"""Проверка обновления пробега."""
		self.car.update_odometer(100)
		self.assertEqual(100, self.car.odometer_reading)

	def test_protection_mileage_reduction(self):
		"""Проверка защиты от уменьшения пробега."""
		self.car.update_odometer(-100)
		self.assertNotEqual(-100, self.car.odometer_reading)

	def test_increase_odometer(self):
		"""Проверка увеличения пробега."""
		self.car.increment_odometer(75)
		self.assertEqual(100, self.car.odometer_reading)

if __name__ == '__main__':
	unittest.main()

