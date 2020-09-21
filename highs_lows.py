import csv

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
        highs.append(filled_high)
        high_previous = filled_high


print(highs)


