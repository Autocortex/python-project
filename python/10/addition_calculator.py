print("Enter 2 values and get the addition: ")
print("Press 'q' for exit.")

while True:
	first_number = input("First number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		ansver = int(first_number) + int(second_number)
	except ValueError:
		print("Letters won't work, please enter numbers!!!")
	else:
		print(ansver)