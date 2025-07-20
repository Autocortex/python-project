prompt = "\nSend 'quit' for exit. "
prompt += "\nEnter the pizza app you want to order: "

#active = True
#while active:
#	topping = input(prompt)
#	if topping.lower() == 'quit':
#		active = False
#	else:
#		print(topping.title(),"add in order.")

while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print(topping.title(),"add in order.")