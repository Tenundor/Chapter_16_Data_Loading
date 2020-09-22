import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'Data/Moscow weather 2019-2020.csv'


with open(filename) as weather_csv:
    reader = csv.reader(weather_csv)
    header_row = next(reader)
    dates, highs, lows = [], [], []

    for row in reader:
        try:
            high_temp = row[12]
            low_temp = row[14]
            date_string = row[5]
            current_date = datetime.strptime(date_string, "%Y-%m-%d")
            high_temp_float = float(high_temp)
            low_temp_float = float(low_temp)
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high_temp_float)
            lows.append(low_temp_float)


print(header_row)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Максимальная и минимальная температуры воздуха \n по дням за 2019 - 2020 годы", fontsize=16)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Температура (С)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

