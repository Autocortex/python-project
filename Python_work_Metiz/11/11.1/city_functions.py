def city_country(city, country, population = ''):
	"""Принимает переменные и форматирует в нужный нам текст."""
	city_country = f"{city},{country}"
	if population:
		full_name = f"{city_country.title()} - population {population}"
	else:
		full_name = city_country.title()
	return full_name