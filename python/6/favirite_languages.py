#favorite_languages = {
#	'jen': 'python',
#	'sarah': 'c',
#	'edward': 'ruby',
#	'phil': 'python',
#     }

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")

#for name,language in favorite_languages.items():
#	print(f"{name.title()}'s favorite language is {language.title()}.")

#for name in favorite_languages.keys():
#	print(name.title())

#for name in favorite_languages:
#	print(name.title())

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#	print(name.title())

#	if name in friends:
#		language = favorite_languages[name].title()
#		print(f"\t{name.title()}, I see you love {language}!")

#if 'erin' not in favorite_languages.keys():
#	print("Erin, please take our poll!\n")

#for name in sorted(favorite_languages.keys()):
#	print(f"{name.title()}, thank you for taking the pooll.")

#print("\tThe following languages have been mentioned:")
#for language in favorite_languages.values():
#set() - множество в котором все переменные должны быть уникальными.
#for language in set(favorite_languages.values()):
#	print(language.title())

#favorite_languages = {
#	'jen': 'python',
#	'sarah': 'c',
#	'edward': 'ruby',
#	'phil': 'python',
#     }

#names = ['jen', 'toma','phil','chris']

#for name in names:
# 	if name in favorite_languages.keys():
 #		print(f"Thank you {name.title()}")
 #	else:
 #		print(f"{name.title( )} take the survey.")


#Создаем словарь опроса.
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

#Перебираем словарь и выводим любимые языки.
for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language is C.")
	else:
		print(f"\n{name.title()}'s favorite languages are:")

    	
	for language in languages:
		if len(languages) == 1:
			print()
		else:
			print(f"\t{language.title()}")


	    
	    
	    	