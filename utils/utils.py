import csv


# importing data from a *csv file:
def get_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    # skip the first row:
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows


def parse_expected_errors(error):
    expected_errors = [error]
    if "|" in error:
        expected_errors = error.split("|")
    return expected_errors
