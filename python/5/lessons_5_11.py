ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for ordinal_number in ordinal_numbers:
	if (ordinal_number == 1):
		print(f"{ordinal_number}st")
	elif (ordinal_number == 2):
		print(f"{ordinal_number}nd")
	elif (ordinal_number == 3):
		print(f"{ordinal_number}rd")
	else:
		print(f"{ordinal_number}th")
