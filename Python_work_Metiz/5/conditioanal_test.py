pizza = 'pepperoni'
print("Is pizza == 'pepperoni'? I predict True.")
print(pizza == 'pepperoni')

print("\nIs pizza != 'pepperoni'? I predict False.")
print(pizza != 'pepperoni')

pizza = 'Caprichoza'
print("\nIs pizza.lower() == 'caprichoza'? I predict True.")
print(pizza.lower() == 'caprichoza')

x = 10
y = 10
print("\nIs x == y? I predict True.")
print(x == y)

print("\nIs x != y? I predict False.")
print(x != y)

x = 10
y = 42
print("\nIs x > y? I predict False.")
print(x > y)

print("\nIs x < y? I predict True.")
print(x < y)

print("\nIs x >= y? I predict False.")
print(x >= y)

print("\nIs x <= y? I predict True.")
print(x <= y)

x = 10
y = 12
print("\nIs (x < y) and (x != y). I predict True.")
print((x < y) and (x != y))

print("\nIs (x != y) or (x >=y). I predict True.")
print((x != y) or (x !=y))

pizzas = ['pepperoni', 'margarita', 'tomarita']
print("\nIs 'margarita' in pizzas? I predict True.")
print('margarita' in pizzas)

pizzas = ['pepperoni', 'margarita', 'tomarita']
pizza = '4 sera'
print("\nIf pizza not in pizzas. I predict pizza 4 sera not in menu.")

if pizza not in pizzas:
	print(f"Pizza {pizza.title()} not in menu.")
