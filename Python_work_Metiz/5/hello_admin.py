usernames = []

if usernames:
	for username in usernames:
		if username.lower() == 'admin':
			print("Hello Admin, would you like to seea status report?")
		else:
			print(f"Hello {username.title()}, thank you for logging in again.")	       
else:
	print("We need to ind some users!")




current_users = ['chris','john','camilla','sasha','tomara','bombastik'] 

new_users = ['Chris','Agent008','CAMilla','tom','Mickrob']

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"Username {new_user} is taken")
	else:
		print(f"You can use username - {new_user}.")

