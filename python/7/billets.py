promt = "'quit' for exit."
promt += "\nPls, your age: "


while True:
	age = input(promt)
	age = int(age)

	if age == 'quit':
		break
	elif age < 3:
		print("Ticket cena - 0$.")
	elif ( age >= 3 ) and ( age < 12 ):
		print("Ticket cena - 10$.")
	elif age > 12:
		print("Ticket cena - 15$.")