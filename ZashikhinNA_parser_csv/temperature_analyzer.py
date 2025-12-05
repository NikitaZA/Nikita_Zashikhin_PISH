import csv
import sys
import argparse
from collections import defaultdict


def analyze_temperature_statistics(file_path, target_month=None):
    """
    Читает CSV-файл, обрабатывает данные и выводит статистику по температуре.

    :param file_path: Путь к входному CSV файлу.
    :param target_month: Необязательный параметр. Если указан, выводится статистика только за этот месяц.
    """
    monthly_stats = defaultdict(list)

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            print(f"\nАнализ файла: {file_path}\n")

            for line_num, row in enumerate(reader, 1):
                if len(row) != 6:
                    print(f" [Ошибка формата] Строка {line_num}: неверное количество столбцов ({len(row)} вместо 6). Строка пропущена.")
                    print(f" > Содержимое: {' | '.join(row)}")
                    continue

                try:
                    month = int(row[1])
                    temperature = int(row[5])

                    if not (1 <= month <= 12):
                        print(f" [Ошибка данных] Строка {line_num}: неверный месяц ({month}). Строка пропущена.")
                        continue
                    if not (-99 <= temperature <= 99):
                        print(f" [Ошибка данных] Строка {line_num}: температура ({temperature}) вне диапазона [-99, 99]. Строка пропущена.")
                        continue

                    monthly_stats[month].append(temperature)

                except ValueError:
                    print(f" [Ошибка формата] Строка {line_num}: не удалось преобразовать данные в числа. Строка пропущена.")
                    print(f" > Содержимое: {' | '.join(row)}")
                    continue

        if not monthly_stats:
            print("\nВ файле не найдено валидных данных о температуре для анализа.")
            return

        # --- Логика вывода статистики ---
        if target_month:
            # Вывод статистики только за указанный месяц
            print("\n---------------------------------")
            print(f"--- Статистика за месяц: {target_month:02d} ---")
            print("---------------------------------")
            if target_month in monthly_stats:
                temps = monthly_stats[target_month]
                avg_temp = sum(temps) / len(temps)
                min_temp = min(temps)
                max_temp = max(temps)

                print(f" Среднемесячная температура: {avg_temp:.2f}°C")
                print(f" Минимальная температура: {min_temp}°C")
                print(f" Максимальная температура: {max_temp}°C")
            else:
                print(" Данные за указанный месяц отсутствуют.")
        else:
            # Вывод полной статистики (по всем месяцам и за год)
            print("\n---------------------------------")
            print("--- Статистика по месяцам ---")
            print("---------------------------------")
            all_temperatures = []

            for month in range(1, 13):
                if month in monthly_stats:
                    temps = monthly_stats[month]
                    all_temperatures.extend(temps)

                    avg_temp = sum(temps) / len(temps)
                    min_temp = min(temps)
                    max_temp = max(temps)

                    print(f"\nМесяц: {month:02d}")
                    print(f" Среднемесячная температура: {avg_temp:.2f}°C")
                    print(f" Минимальная температура: {min_temp}°C")
                    print(f" Максимальная температура: {max_temp}°C")
                else:
                    print(f"\nМесяц: {month:02d}")
                    print(" Данные отсутствуют.")

            if all_temperatures:
                print("\n-----------------------------")
                print("--- Статистика за год ---")
                print("-----------------------------")
                yearly_avg = sum(all_temperatures) / len(all_temperatures)
                yearly_min = min(all_temperatures)
                yearly_max = max(all_temperatures)

                print(f"\n Среднегодовая температура: {yearly_avg:.2f}°C")
                print(f" Минимальная температура: {yearly_min}°C")
                print(f" Максимальная температура: {yearly_max}°C")

    except FileNotFoundError:
        print(f"ERROR: Файл не найден по пути: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Произошла непредвиденная ошибка: {e}")
        sys.exit(1)


def main():
    """
    Основная функция для разбора аргументов командной строки и запуска анализа.
    """
    parser = argparse.ArgumentParser(
        description="Консольное приложение для анализа статистики температуры из CSV файла.",
        epilog="Пример использования: python main.py -f temperature_data.csv -m 7"
    )

    parser.add_argument(
        '-f', '--file',
        type=str,
        required=True,
        help="Входной файл CSV для обработки."
    )

    parser.add_argument(
        '-m', '--month',
        type=int,
        choices=range(1, 13),
        metavar='<номер месяца>',
        help="Номер месяца для вывода статистики (от 1 до 12). Если не указан, выводится статистика за год."
    )

    args = parser.parse_args()
    analyze_temperature_statistics(args.file, args.month)


if __name__ == "__main__":
    main()