def describe_city(city = 'reykjavik', country = 'iceland'):
	"""Выводит название города и Стану."""
	print(f"{city.title()} is in {country.title()}.")

describe_city()
describe_city("Kiyv", 'Ukraine')
describe_city("Riode")