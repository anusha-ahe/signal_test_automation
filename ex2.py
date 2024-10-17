import csv
import re
from collections import defaultdict


def create_test_case_dict(csv_file_path, signal_name):
    test_name = {}
    print("Creating test case dict for signal: {} from CSV file: {}".format(signal_name, csv_file_path))
    try:
        with open(csv_file_path, mode='r') as file:
            rows = list(csv.reader(file))
            columns = rows[0][1:]
            values = rows[1][1:]
            if signal_name not in test_name:
                test_name[signal_name] = {}
            for col_name, value in zip(columns, values):
                test_name[signal_name][col_name] = value or 'None'
            print("Test case dict created for {}: {}".format(signal_name, test_name[signal_name]))
            print(generate_signal_menu_mapping(columns))
    except Exception as e:
        print("Error occurred while reading the CSV: {}".format(e))


def generate_signal_menu_mapping(data_list):
    result = defaultdict(list)
    for item in data_list:
        item = item.replace('-', '_')
        match = re.match(r'(\d+)', item)
        if match:
            key = match.group(0)
            result[key].append(item)
    result = {key: sorted(values) for key, values in result.items()}
    result = {value[0]: value for key, value in result.items()}
    return result


if __name__ == "__main__":
    csv_file_path = "D:\\signal\\test-signal\\test_signal\\Generate.sikuli\\signal_sheet.csv"
    signal_name = "1L1"
    create_test_case_dict(csv_file_path,signal_name)