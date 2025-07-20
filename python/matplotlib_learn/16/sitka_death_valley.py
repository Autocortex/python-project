import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename_1='data/death_valley_2018_simple.csv'
filename_2='data/sitka_weather_2018_simple.csv'

dates_1, dates_2 = [], []
high_1, lows_1 = [], []
high_2, lows_2 = [], []


with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_1.append(current_date)
            high_1.append(high)
            lows_1.append(low)

with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        high_2.append(high)
        lows_2.append(low)
        dates_2.append(current_date)

all_highs = high_1 + high_2
all_lows = lows_1 + lows_2
y_min = min(all_lows)
y_max = max(all_highs)


plt.style.use('seaborn-v0_8')
fig, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(dates_1, high_1, c = 'red', alpha = 0.5)
ax1.plot(dates_1, lows_1, c = 'blue', alpha = 0.5)
ax1.fill_between(dates_1, high_1, lows_1, facecolor = 'blue', alpha = 0.1)
ax1.set_title('Death Valley - 2018', fontsize = 10)
ax1.set_ylim(y_min, y_max)
ax1.set_ylabel('Temperatures', fontsize = 16)
ax1.legend(['High','Low'])

ax2.plot(dates_2, high_2, c = 'red', alpha = 0.5)
ax2.plot(dates_2, lows_2, c = 'blue', alpha = 0.5)
ax2.fill_between(dates_2, high_2, lows_2, facecolor = 'blue', alpha = 0.1)
ax2.set_title('Sitka - 2018', fontsize = 10)
ax2.set_ylim(y_min, y_max)
ax2.set_ylabel('Temperatures', fontsize = 16)
ax2.legend(['High', 'Low'])

title = 'Comparison of temperatures'
fig.suptitle(title, fontsize = 16)
fig.autofmt_xdate()
plt.xlabel('', fontsize = 10)

plt.show()

