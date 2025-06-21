import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#for index, column_header in enumerate(header_row):
#   print(index, column_header)

    dates, humidity = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        hmd = float(row[3])
        humidity.append(hmd)
        dates.append(current_date)

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, humidity, c = 'red', alpha = 0.5)
    plt.title('Daily humidity-2018.', fontsize = 24)
    plt.xlabel('',fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Humidity', fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
    plt.show()