from pathlib import Path

def count_word_in_book(filepath, word):
	"""
	Открывает файл и считывает, сколько
	в нем повторяется word.
	"""
	path = Path(filepath)
	contents = path.read_text(encoding = 'utf-8')
	print(contents.lower().count(f"{word} "))

filepath = 'peppermint.txt'
word = 'the'
count_word_in_book(filepath, word)