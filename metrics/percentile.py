import csv
import numpy as np
import pandas as pd


def read_csv(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        data = csv.reader(file)
        headers = next(data)
        return [list(row) for row in data], headers


def write_csv(data, headers, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)


csv_filename = 'voice-listener_metrics.csv'
new_csv_filename = 'voice-listener_percentiles.csv'

original_data, headers = read_csv(csv_filename)

normalized_data = []

ascending_column = ['time_to_close_issues', 'time_to_comment_issues', 'time_to_close_PRs', 'time_to_comment_PRs', 'vulnerabilities', 'outdated_versions']

for col_index in range(len(headers)):
    column_data = [row[col_index] for row in original_data]
    if col_index > 1:
        numeric_data_list = [float(x) for x in column_data if x != "-1.0"]
        # ascending by default
        if numeric_data_list:
            sorting_indices = np.argsort(numeric_data_list)
            sorting_data_list = [None] * len(numeric_data_list)
            for index, x in enumerate(sorting_indices):
                sorting_data_list[x] = index + 1
            index = 0
            scaled_column = []
            for x in column_data:
                if x != "-1.0":
                    if col_index not in ascending_column:
                        scaled_column.append(f"{(sorting_data_list[index] / 10) :.1f}")
                    else:
                        scaled_column.append(f"{((len(numeric_data_list) + 1 - sorting_data_list[index]) / 10):.1f}" )
                    index += 1
                else:
                    scaled_column.append("N/A")
            normalized_data.append(scaled_column)
    else:
        normalized_data.append(column_data)

transposed_data = []

for row in zip(*normalized_data):
    transposed_data.append(list(row))

write_csv(transposed_data, headers, new_csv_filename)

df = pd.read_csv(new_csv_filename)

print(f"Processed data has been successfully written to {new_csv_filename}")

