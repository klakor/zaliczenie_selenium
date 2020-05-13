import os
import csv


# importing data from a *csv file:
def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    # Pomijam pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


def error_split_text():
    expected_errors = [error]
    if "|" in error:
        expected_errors = error.split("|")
