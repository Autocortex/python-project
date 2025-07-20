import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c =y_values, cmap=plt.cm.Blues, s=10)

ax.set_title('Cube Numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

plt.show()