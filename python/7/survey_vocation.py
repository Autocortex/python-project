vocations = {}

active = True

while active:
	name = input("\nWhat is yor name? ")
	response = input("\nHow will you spend your vacation? ")

	vocations[name] = response

	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		active = False

print("---Poll Results---")
for name, response in vocations.items():
	print(f"{name}\n{response}")
