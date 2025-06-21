import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

from die import Die

die_1 = Die(6)
die_2 = Die(6)


results = [die_1.roll()+die_2.roll() for i in range(1000)]
max_sides = die_1.num_sides + die_2.num_sides
counted = Counter(results)
frequencies = [counted[value] for value in range(2, max_sides+1)]

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(list(range(2, max_sides + 1)), frequencies, linewidth=1)
ax.set_xticks(np.arange(2,max_sides+1,1))
plt.show()