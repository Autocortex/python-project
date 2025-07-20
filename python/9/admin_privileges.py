from user import User

class Privileges():
	"""Представляет все привелегии пользователя."""

	def __init__(self, privileges = []):
		"""Инициализирует атрибут privileges."""
		self.privileges =  [
							'-u can deleted users',
							'-u can banned users',
							'-u can add massage'
							]

	def show_privileges(self):
		"""Показывает привелегии администратора."""
		print("Your privileges: ")
		for privilege in self.privileges:
			print(f"{privilege}")

class Admin(User):
	"""Представляет аспекты пользователя с особыми привелегиям"""

	def __init__(self, first_name, last_name, age, nick):
		"""Инициализирует родительские атрибуты."""
		super().__init__(first_name, last_name, age, nick)
		self.privileges = Privileges()