import csv

filename = 'Data/Moscow weather 2019-2020.csv'
with open(filename) as weather_csv:
    reader = csv.reader(weather_csv)
    header_row = next(reader)
    highs = []
    for row in reader:
        highs.append(row[12])

print(highs)
