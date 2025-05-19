with open('guest.txt', 'a') as file_object:
	active = True
	while active:
		guest = input("Your name:")
		print("'q' for exit")
		guest_hello = f"Hello, {guest.title()}\n"
		print(guest_hello)
		file_object.write(guest_hello)
		if guest == 'q':
			active = False
