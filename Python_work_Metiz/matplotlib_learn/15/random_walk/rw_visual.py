import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построениие случайного блуждания.
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
