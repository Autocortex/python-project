def get_city_counrty(city, country):
	"""Возвращает аккуратно отфарматированные данные."""
	mod_city_country = f"{city}, {country}"
	return mod_city_country.title()

while True:
	print("\nPlease tell me your City and Country: ")
	print("(enter 'q' for exit)")

	city = input("City: ")
	if city == 'q':
		break

	country = input("Country: ")
	if country == 'q':
		break

	city_country = get_city_counrty(city, country)
	print(f"\n{city_country}")



