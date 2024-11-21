import csv
import math


def task(file_path: str):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
        count = len(data)
        entropy_sum = 0

        for row in data:
            for cell in row:
                cell_value = cell
                if cell_value != '0':
                    digit_value = float(cell_value) / (count - 1)
                    entropy_sum += -digit_value * math.log2(digit_value)

    return round(entropy_sum, 1)


if __name__ == '__main__':
    csv_file_path = 'task3.csv'
    entropy = task(csv_file_path)
    print(entropy)
