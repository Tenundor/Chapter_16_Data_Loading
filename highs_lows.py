import csv
from matplotlib import pyplot as plt


filename = 'Data/Moscow weather 2019-2020.csv'


def fill_empty_string(string, filler):
    """Assigns to the "String" variable the value of the "filler", if "string" is empty"""
    if string == '':
        return filler
    else:
        return string


with open(filename) as weather_csv:
    reader = csv.reader(weather_csv)
    header_row = next(reader)
    highs = []
    high_previous = 0
    for row in reader:
        filled_high = fill_empty_string(row[12], high_previous)
        high_float = float(filled_high)
        highs.append(high_float)
        high_previous = filled_high


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

plt.title("Максимальная температура воздуха по дням за 2019 год", fontsize=21)
plt.xlabel('', fontsize=16)
plt.ylabel("Температура (С)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

