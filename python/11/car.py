class Car():
	"""Описание машины"""

	def __init__(self, make, model, odometer_reading = 0):
		"""Инициализирует аргументы make, model, odometer_reading."""
		self.make = make
		self.model = model
		self.odometer_reading = odometer_reading

	def update_odometer(self,mileage):
		"""Обновляет пробег, но не позовляет уменьшать его."""
		if mileage < 0:
			self.odometer_reading = 0
		else:
			self.odometer_reading = mileage
			return self.odometer_reading

	def increment_odometer(self, miles):
		"""Увеличивает пробег"""
		if miles < 0:
			self.odometer_reading
		else:
			self.odometer_reading += miles
			return self.odometer_reading