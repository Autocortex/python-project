pets_0 = {
    'name': 'barsik',
	'species': 'cat',
	'owner': 'John',
}

pets_1 = {
    'name': 'sir',
	'species': 'dog',
	'owner': 'Sara',
}

pets_2 = {
    'name': 'leo',
	'species': 'snake',
	'owner': 'Chris',
}

pets = [pets_0, pets_1, pets_2]

for pet in pets:
	print(f"\nName: {pet['name'].title()}.\n"
		  f"Animal species: {pet['species'].title()}.\n"
		  f"Owner: {pet['owner'].title()}.\n"
		  )