def make_sandwich(*toppings):
	"""Выводит произвольное количество компонентов сэндвича."""
	print("\nMake sandwich with:")
	for topping in toppings:
		print(f"-{topping}")

make_sandwich('cheese', 'cucumber', 'tomate')
make_sandwich('salat', 'ketchup')
make_sandwich('fish')