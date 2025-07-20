cities = {
	'Warsaw': {
	'country': 'Poland',
	'population': '1.865 mln',
	'fact': 'From 1918 to 1939, Warsaw was the capital of the Polish Republic.',
	},
	'Kiev': {
	'country': 'Ukrain',
	'population': '2.952 mln',
	'fact': 'The Kyiv metro is one of the oldest in Europe.',
	},
	'Paris': {
	'country': 'France',
	'population': '2,103 mln',
	'fact': 'There is an Eiffel Tower there.',
	},
}

for city, information in cities.items():
	print(f"City - {city}.\n"
	      f"Population - {information['population']}.\n"
	      f"Fact - {information['fact']}\n")