from pathlib import Path

def conclusion_text (filepath):
	"""Читает и выводит текст из файла."""
	try:
		path = Path(filepath)
		contents = path.read_text()
	except FileNotFoundError:
		pass
	else:
		print(contents)

filepath = 'catss.txt'
conclusion_text(filepath)

filepath = 'dogs.txt'
conclusion_text(filepath)
