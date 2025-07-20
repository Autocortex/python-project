prompt = "How many seats would you like to reserve a table for? "

seats = input(prompt)
seats = int(seats)

if seats > 8:
	print("Sorry, but you have to wait.")
else:
	print("The table is ready.")