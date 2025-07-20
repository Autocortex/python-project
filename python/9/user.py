class User():
	"""Простая модель пользователя"""

	def __init__(self, first_name, last_name, age, nick):
		"""Инициализирует атрибуты first_name, last_name, age, nick."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.nick = nick
		self.login_attempts = 0

	def describe_user(self):
		"""Выводит информацию о пользователе."""
		print(self.first_name.title())
		print(self.last_name.title())
		print(self.age)
		print(self.nick)

	def greet_user(self):
		"""Вывод привествия для пользователя."""
		print(f"Hello, {self.nick}.")

	def increment_login_attempts(self):
		"""Увеличивает значение числа входов на 1."""
		self.login_attempts += 1

	def info_login_attempts(self):
		"""Выводит информацию о количестве попыток входа."""
		print(f"Login attempt: {self.login_attempts}")

	def reset_login_attempts(self):
		"""Обнуляет количество входов в систему."""
		self.login_attempts = 0


