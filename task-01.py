"""
This program calculates total and average salaries from a text file and handles 
errors for missing or invalid files.
"""

import pathlib as pl

with open('salaries.txt', 'w+', encoding='utf-8') as f:                   # створюємо файл з можливістю його прочитати та встановленим кодуванням
    f.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')  # вносимо дані в файл, кожного співробітника в новому рядку

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    name, salary = line.split(',')                        # сплітимо по кожному рядку окремо
                    total += int(salary)
                    count +=1                                             # підрахували кількість рядків
                except Exception as e:                                    # виключили можливість зупинки програми, якщо якийсь рядок відсутній або має не правильний формат
                    print(f"Error in file: {e}")
        average = int(total / count) if count > 0 else 0                  # одразу виключили ділення на нуль
        return total, average
    except Exception as e:                                                # виключили можливість помилки відсутності/пошкодження файлу або будь-яку іншу
        print(f"Function error: {e}")

salaries_path = pl.Path("salaries.txt").absolute()                        # визначили шлях до файлу
total, average = total_salary(salaries_path)
print(f"Total salary amount: {total}, Average salary amount: {average}")