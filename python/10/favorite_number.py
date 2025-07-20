import json
from pathlib import Path 

filename = 'favorite_number.json'

try:
	path = Path(filename)
	contents = path.read_text()
	number = json.loads(contents)
except FileNotFoundError:
	number = input("Введите любимое число: ")
	path = Path(filename)
	contents = json.dumps(number)
	path.write_text(contents)
else:
	print(number)