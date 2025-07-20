prompt = "Tell me something, and i will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message.lower() =='quit':
		active = False
	else:
		print(message)