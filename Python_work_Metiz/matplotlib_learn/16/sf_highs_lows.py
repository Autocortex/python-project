import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sanfrancisko_1921_2025.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #for index, column_header in enumerate(header_row):
    #    print(index,column_header)
    # 2 - date, 10 - tmax, 11 - tmin
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        #Calculate degrees in Celcius for highs and lows.
        try:
            high = int(row[10])
            low = int(row[11])
        except ValueError:
            print(f"Not value for {current_date}")
        else:
            high_c = (high - 32)*(5/9)
            rhigh_c = round(high_c, 1)
            low_c = (low - 32) * (5 / 9)
            rlow_c = round(low_c, 1)
            #Add to the lists.
            dates.append(current_date)
            highs.append(rhigh_c)
            lows.append(rlow_c)

    max_h = max(highs)
    index_max = highs.index(max_h)
    max_d = dates[index_max]

    min_h = min(lows)
    index_min = lows.index(min_h)
    min_d = dates[index_min]


    fig, ax = plt.subplots(figsize = (15,6))
    ax.plot(dates, highs, c = 'red', alpha = 0.5)
    ax.plot(dates, lows, c = 'blue', alpha = 0.5)
    ax.scatter(max_d, max_h, c = 'darkred', label = 'Max')
    ax.scatter(min_d, min_h, c = 'darkblue', label = 'Min')
    ax.annotate(f"{max_h}°C", xy = (max_d, max_h + 0.5), fontsize = 10, color = 'darkred')
    ax.annotate(f"{min_h}°C", xy = (min_d, min_h - 2), fontsize = 10, color = 'darkblue')
    ax.fill_between(dates,lows, highs, facecolor = 'blue', alpha = 0.1)
    fig.autofmt_xdate()
    plt.title('San Francisko 1920-2025', fontsize = 16)
    plt.ylabel('Temperatures', fontsize = 16)
    plt.show()