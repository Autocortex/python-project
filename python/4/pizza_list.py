pizza_list = ['caprichoza','Margarita','Frutti de Mara']
for pizza in pizza_list:
	print(f"I like {pizza.title()} pizza!")

print("\nI realle love pizza")

friend_pizzas = pizza_list[:]
pizza_list.append('4 ser')
friend_pizzas.append('Salsa')

print("\nMy favorite pizzas are:")
for pizza in pizza_list[:]:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
	print(friend_pizza)