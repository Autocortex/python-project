#players = ['charles', 'martina', 'machael', 'florence', ' eli']
#print(players[0:4])
players = ['charles', 'martina', 'machael', 'florence', 'eli']
print("Here are first three players on my team:")
for player in players[0:3]:
	print(player.title())

print("The first three items in the list are:")
for player in players[:3]:
	print(player.title())

print("The items from the middle of the list are:")
for player in players[1:4]:
	print(player.title())

print("The last three items in the list are:")
for player in players[-3:]:
	print(player.title())