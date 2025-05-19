import unittest
from city_functions import city_country

class NameTestCase(unittest.TestCase):
	"""Тестирует функцию city_country."""

	def test_city_country(self):
		"""Проверяем правильно строки."""
		formatted_name = city_country('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago,Chile')

	def test_city_country_population(self):
		"""Проверяем, правильно ли функция принимает 3 аргумента."""
		formatted_name = city_country(
			'santiago', 'chile', population = '5000000')
		self.assertEqual(formatted_name, 'Santiago,Chile - population 5000000')
if __name__ == '__main__':
	unittest.main()