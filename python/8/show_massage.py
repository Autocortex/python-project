messages = ['hello', 'how are you', 'nice to meet you']
sent_messages = []

def send_messages(messages, sent_messages):
	"""Выводит каждое сообщение в списке messages.
	   Помещает их в новый список send_messages."""
	while messages:
		message = messages.pop()
		print(f"\n{message}")
		sent_messages.append(message)

send_messages(messages[:], sent_messages)
print("\n\tList:\n",messages)



