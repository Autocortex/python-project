import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, humidity = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        hmd = float(row[3])
        humidity.append(hmd)
        dates.append(current_date)

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(dates, humidity, c = 'blue', alpha = 0.5)
    plt.title('Daily humidity - 2018', fontsize = 16)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel('Humidity', fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 10)
    plt.show()