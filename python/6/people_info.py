people_0 = {
    'first_name': 'Tomara',
    'last_name': 'Peteichuk',
    'age': '25',
    'city': 'Warsaw',
    }

people_1 = {
    'first_name': 'Sasha',
    'last_name': 'Ivanow',
    'age': '28',
    'city': 'Warsaw',
}

people_2 = {
    'first_name': 'Natalia',
    'last_name': 'Nuhalova',
    'age': '30',
    'city': 'Warsaw',
}

people_all = [people_0, people_1, people_2]

for people in people_all:
    print(f"First name - {people['first_name'].title()}"
        f"\nLast name - {people['last_name'].title()}"
        f"\nAge - {people['age']}"
        f"\nCity - {people['city'].title()}\n")

