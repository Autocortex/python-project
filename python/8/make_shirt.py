def make_shirt(text = 'I love python', size = 'L'):
	"""Выводит размер и текст на футболке."""
	print(f"Your size - {size} and yor text on shirt: {text}")

make_shirt('Crazy boy', 'M')
make_shirt(size = 'L', text = 'Crazy boy')
make_shirt('Human')
make_shirt(size = 'M')