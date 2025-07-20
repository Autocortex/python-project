from random import choice


def generator_ticket(ticket_lenght = 4):
	"""
	Генерирует билеты, до тех пор пока не попадется победный.
	Дает нам результат, количество попыток, которое понадобилось.
	"""
	ticket = [1, 2, 3, 'a', 4, 5, 'g', 7, 9, 'c', 3, 'v', 1, 't', 2]
	my_ticket = []
	winning_tick = [1,'a',7,'c']
	attempts = 0

	while True:
		while len(my_ticket) < ticket_lenght:
			choice_item = choice(ticket)
			if choice_item not in my_ticket:
				my_ticket.append(choice_item)
		attempts += 1
		print(my_ticket)

		if set(my_ticket) == set(winning_tick):
			print("You win")
			break
		else:
			my_ticket.clear()

	return attempts
	print(attempts)

info = generator_ticket()
print(info)


