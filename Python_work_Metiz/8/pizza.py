def make_pizza(size, *toppings):
	"""Вывод описание пиццы."""
	print(f"\nMaking a {size}-inch  pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")
