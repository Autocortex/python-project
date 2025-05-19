def make_car(model, manafacturer, **info):
	"""Сохраняет информацию об автомабиле в словаре."""
	info['model'] = model
	info['manafacturer'] = manafacturer
	return info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)