number = input("Enter number: ")
number = int(number)

if ( number % 10 ) == 0:
	print(f"{number} multiples of 10.")
else:
	print(f"{number} is not multiples of 10.")