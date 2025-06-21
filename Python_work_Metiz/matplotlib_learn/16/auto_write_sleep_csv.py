import csv
from datetime import datetime

filename = 'data/sleep_log.csv'

# Проверка: нужно ли создавать заголовок
try:
    with open(filename, 'x', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["DATE", "BEGSLEEP", "ENDSLEEP", "GRADE"])
except FileExistsError:
    pass  # файл уже существует, не создаём заголовок

# Запрос данных у пользователя
date = input("Дата (например, 2025-06-20): ")
beg = input("Во сколько уснул? (HH:MM): ")
end = input("Во сколько проснулся? (HH:MM): ")
grade = input("Оценка сна (1-10): ")

# Запись в CSV
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow([date, beg, end, grade])

print("Запись добавлена в", filename)
