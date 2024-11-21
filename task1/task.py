import csv
import sys


def get_csv(file_path, row_number, col_number):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if row_number < 1 or row_number > len(rows):
                return f"Ошибка: строка {row_number} вне диапазона."

            if col_number < 1 or col_number > len(rows[row_number - 1]):
                return f"Ошибка: столбец {col_number} вне диапазона."

            value = rows[row_number - 1][col_number - 1]
            return f"Значение: {value}"
    except FileNotFoundError:
        return f"Ошибка: файл {file_path} не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"


def main():
    if len(sys.argv) != 4:
        return "Использование: python script.py <путь к файлу> <номер строки> <номер колонки>"

    file_path = sys.argv[1]
    row_number = int(sys.argv[2])
    col_number = int(sys.argv[3])

    result = get_csv(file_path, row_number, col_number)
    return result


if __name__ == "__main__":
    result = main()
    print(result)
