#age = 12

#if age < 4:
#	print("Your admission cost $0.")
#elif age < 18:
#	print("Your admission cost $25.")
#else:
#	print("Your admission cost $40.")

age = 68

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >=65:
	price = 20
#else:
#	price = 20

print(f"Your admission cost ${price}.")