"""
This script recursively displays the structure of a specified directory in colors.
"""

import pathlib, sys
from colorama import Fore, Style, init
init(autoreset=True)

def dir_structure(path: pathlib.Path, indent: str = ""):         # спочатку робимо функцію для зображення структури папки, одразу задаємо, що вона має порожній відступ по дефолту
    if not path.exists() or not path.is_dir():                   # одразу вказуємо, що якщо шлях не існує або не є папкою, то виводимо помилку  
        print(f"{Fore.RED}ERROR: {Fore.BLUE}{path} {Fore.RED}does not exist or is not a directory.")
        return
    for item in path.iterdir():                                  # вказуємо, що будемо працювати із переліком усіх файлів в папці
        if item.is_dir():                                        # якщо це папка (директорія), то виводимо її назву в синьому кольорі
            print(Fore.BLUE + f"{indent}{item.name}/")
            dir_structure(item, indent + "    ")                 # викликаємо функцію, щоб показати вміст папки із відступом
        elif item.is_file():                                     # якщо це файл, то виводимо його назву в зеленому кольорі
            print(Fore.GREEN + f"{indent}{item.name}")
        else:
            print(Fore.YELLOW + f"{indent}{item.name}")          # усі інші винятки жовтим кольором

def display_structure():
    if len(sys.argv) != 2:                                       # перевіряємо, чи введено обидва аргументи: назва файла зі скриптом та шлях
        print(f"{Fore.RED}ERROR: directory path must be passed.")
        sys.exit()
    dir_path = pathlib.Path(sys.argv[1])                         # вказуємо, що другий аргумент це шлях до папки
    dir_structure(dir_path)                                      # передаємо цей другий аргумент у функцію, щоб показати структуру

display_structure()