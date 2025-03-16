"""
This program reads data from a text file, processes each line into a dictionary, 
and handles errors such as missing files or invalid data format.
"""

import pathlib as pl

with open('cats.txt', 'w+', encoding='utf-8') as f:                  # створюємо файл з можливістю читати його та вказуємо кодування
    f.write(                                                         # використала """, щоб не було довжелезного рядка в скрипті
        """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5"""
    )

def get_cats_info(path):
    cats_info = []                                                   # вказали, що хочемо отримати список
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    cat_id, name, age = line.strip().split(',')                       # окрім спліта по комам виключаємо зайві пробіли в майбутньому через strip, бо працюємо з текстом
                    cats_info.append({'id': cat_id, 'name': name, 'age': int(age)})   # показали, що прагнемо отримати словники та задали назви ключів
                except Exception as e:                                                # обробили помилки в файлі, якщо будуть відсутні чи невірні якісь дані
                    print(f"Error in file: {e}")
        return cats_info
    except Exception as e:                                           # обробили помилки під час виконання самої функції, якщо шлях невірний, чи файл не існує/пошкоджений
        print(f"Function error: {e}")

cats_path = pl.Path('cats.txt').absolute()                           # знайшли абсолютний шлях до файлу
cats_info = get_cats_info(cats_path)
print(cats_info)