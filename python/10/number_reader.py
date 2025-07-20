import json
from pathlib import Path

filename = 'numbers.json'
path = Path(filename)
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)