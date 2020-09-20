import csv

filename = 'Data/Moscow weather 2019-2020.csv'
with open(filename) as weather_csv:
    reader = csv.reader(weather_csv)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
