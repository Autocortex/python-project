import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Проверяем класс Employee на ошибки."""

	def setUp(self):
		"""Присваиваем значения атрибутам"""
		self.empl1 = Employee('Oleksandr', 'Ivanov', 10000)


	def test_give_default_raise(self):
		"""Проверяет изменение оклада по умолчанию."""
		self.assertEqual(15000, self.empl1.give_raise())

	def test_give_custom_raise(self):
		"""Проверяет на заданный оклад."""
		self.assertEqual(17500, self.empl1.give_raise(7500))

if __name__ == '__main__':
    unittest.main()