rivers_countries = {'nile': 'egypt', 'dnepr': 'ukraine', 'gang': 'india'}

for river,countre in rivers_countries.items():
	print(f"The {river.title()} runs through {countre.title()}.")

for river in rivers_countries.keys():
	print(river.title())

for countre in rivers_countries.values():
	print(countre.title())