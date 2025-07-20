with open('survey.txt', 'a') as file_object:
	while True:
		print("(Press 'q' for exit.)")
		ansver = input("Why do you like programming? ")
		if ansver == 'q':
			break
		file_object.write(f"{ansver}\n")
		
