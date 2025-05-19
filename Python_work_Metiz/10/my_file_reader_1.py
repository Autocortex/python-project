from pathlib import Path

def reader_file(txt_path, lines = []):
	"""Получает ссылку на файл и делает из него список для работы."""
	path = Path(txt_path)
	contents = path.read_text()
	lines = contents.splitlines()
	return lines


def modified_file(lines):
	"""Изменяет исходный список."""
	for line in lines:
		new_line = line.replace('Python', 'C++')
		print(new_line)


show_my_txt = reader_file('learning_python.txt')
modified_file(show_my_txt)
