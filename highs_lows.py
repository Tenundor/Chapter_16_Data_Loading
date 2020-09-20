import csv

filename = 'Data/sitka_weather_2018_full.csv'
with open(filename) as weather_csv:
    reader = csv.reader(weather_csv)
    header_row = next(reader)
    print(header_row)
