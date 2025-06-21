import csv
from datetime import datetime

from matplotlib import pyplot as plt

class BuildGraph():
    """Class for searching indexes in any weather csv files."""

    def __init__(self):
        self.filename = self.input_path()

    def run(self):
        """Run search index in file"""
        while True:
            try:
                dates, highs, lows, city = self.open_csv()
                self.build_graph(dates, highs, lows, city)
            except FileNotFoundError:
                print("Pls check you file path.")
                self.filename = self.input_path()
            else:
                break

    def build_graph(self, dates, highs, lows, city):
        """Build Graph."""
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots(figsize=(15, 6))
        ax.plot(dates, highs, c='red', alpha=0.5)
        ax.plot(dates, lows, c='blue', alpha=0.5)
        ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
        max_h, min_h, max_d, min_d = self._get_min_max_values(highs, lows, dates)
        ax.scatter(max_d, max_h, c='darkred', label='Max')
        ax.scatter(min_d, min_h, c='darkblue', label='Min')
        ax.annotate(f"{max_h}°C", xy=(max_d, max_h + 1), fontsize=10, color='darkred')
        ax.annotate(f"{min_h}°C", xy=(min_d, min_h - 1), fontsize=10, color='darkblue')
        fig.autofmt_xdate()
        plt.title(f"{city}")
        plt.ylabel('Temperatures', fontsize = 16)
        plt.show()

    def _get_min_max_values(self, highs, lows, dates):
        """Calculates minimum and maximum temperatures on a graph."""
        max_h = max(highs)
        index_max = highs.index(max_h)
        max_d = dates[index_max]

        min_h = min(lows)
        index_min = lows.index(min_h)
        min_d = dates[index_min]

        return max_h,min_h, max_d, min_d

    def open_csv(self):
        """Work with .csv file."""
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            rows = list(reader)
            tmax_row, tmin_row, name_row, date_row = self._sorting_header_row(header_row)
            city = self._gen_name_city(name_row, rows)
            dates, highs, lows = self._get_dates_temperatures(date_row, tmax_row, tmin_row, rows)
            self._not_contained(header_row)
            return dates, highs, lows, city


    def _get_dates_temperatures(self, date_row, tmax_row, tmin_row, rows):
        """Get dates and temperatures."""
        dates, highs, lows = [], [], []
        for row in rows:
            try:
                current_date = datetime.strptime(row[date_row], '%Y-%m-%d')
                high_f = int(row[tmax_row])
                low_f = int(row[tmin_row])
            except ValueError:
                print(f"Not value for {current_date}")
            else:
                high, low = self._get_celcius(high_f, low_f)
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
        return dates, highs, lows

    def _get_celcius(self, high_f, low_f):
        """Converts temperature from Fahrenheit to Celsius"""
        high_c = (high_f - 32) * (5 / 9)
        high = round(high_c, 1)
        low_c = (low_f - 32) * (5 / 9)
        low = round(low_c, 1)
        return high, low

    def _gen_name_city(self, name_row, rows):
        """Generate name City."""
        gen_full_name = (row[name_row] for row in rows)
        for full_name in gen_full_name:
            name = full_name.split(',')[0].title()
            return name

    def _sorting_header_row(self,header_row):
        """Sorting header row."""
        for index, value in enumerate(header_row):
            if value == 'TMAX':
                tmax_row = index
            elif value == 'TMIN':
                tmin_row = index
            elif value == 'NAME':
                name_row = index
            elif value == 'DATE':
                date_row = index
        return tmax_row, tmin_row, name_row, date_row

    def _not_contained(self, header_row):
        """File  not contained TMAX and(or) TMIN"""
        tmax, tmin = 'TMAX', 'TMIN'
        if tmax not in header_row and tmin not in header_row:
            print('File not contained "TMAX" and "TMIN"')
        elif tmin not in header_row or tmax not in header_row:
            print('File not contained "TMAX" or "TMIN"')


    def input_path(self):
        filename = input('Pls input filepath: ')
        return filename


si = BuildGraph()
si.run()


