class Restaurant():
	"""Простая модель ресторана."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты restaurant_name и cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Выводит два атрибута."""
		print(f"{self.restaurant_name.title()}")
		print(f"Type of cuisine: {self.cuisine_type}.")

	def open_restaurant(self):
		"""Выводит что ресторан открыт."""
		print(f"{self.restaurant_name.title()} open.")

	def number_serv(self):
		"""Выводит информацию о посетителях"""
		print(f"Number served: {self.number_served}")

	def set_number_served(self, reserv_seats):
		"""Изменяет колиичество забранированных мест."""
		self.number_served = reserv_seats

	def increment_number_served(self, seats):
		"""Увеличивает количество забронированных мест на заданную величину."""
		self.number_served += seats

class IceCreamStand(Restaurant):
	"""Представляет аспекты ресторана, специфические для киоска с мороженным."""

	def __init__(self, restaurant_name, cuisine_type):
		"""
	    Инициализирует атрибуты класса родителя.
	    Затем инициализируем атрибуты, специфические для киосков с мороженным.
	    """
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['blacberry', 'cherry', ' mango']

	def describe_flavors(self):
		"""Выводит информацию о сортах мороженного."""
		for flavor in self.flavors:
			print(f"Flavors: {flavor}")
  