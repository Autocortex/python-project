#Создаем список сэндвичей и конечный список, куда будем переносить текущий.
sandwich_orders = ['Sansara', 'Pastrami', 'Qauri', 'Pastrami', 'Pastrami']
finished_sandwiches = []

print("\nWe not have Pastrami!")
while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')

#Создаем список, в котором будем перебирать элементы первого списка.
while sandwich_orders:
#Высовываем каждый элемент из списка и назначаем переменную к элементу.
	sandwich = sandwich_orders.pop()
	print(f"I made you {sandwich} sandwich.")

#Перемещаем элементы в новый список.
	finished_sandwiches.append(sandwich)

print("\nSandwiches:")
#Перебираем новый список и выводим на экран каждый элемент списка.
for finished_sandwich in finished_sandwiches:
	print(f"\t{finished_sandwich}")

