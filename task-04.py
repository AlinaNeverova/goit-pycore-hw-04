"""
Simple CLI assistant bot that manages contacts.
Supports adding, changing, displaying, and listing contacts.
"""
# Спочатку окремо створюємо необхідні функції для помічника
def parse_input(user_input):                                 # Парсер команд користувача
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

def add_contact(args, contacts):                             # Функція, що додає нові контакти
    if len(args) != 2:                                       # Видає помилку, якщо аргументів не 2
        return "Error: Invalid format. Use 'add [name] [phone]'."
    name, phone = args
    contacts[name] = phone                                 
    return "Contact added."

def change_contact(args, contacts):                          # Функція, що змінює існуючий контакт
    if len(args) != 2:                                       # Знову перевірка на помилку, якщо аргументів не 2
        return "Error: Invalid format. Use 'change [name] [new phone]'."
    name, phone = args
    if name in contacts:                                     # Якщо контакт є в словнику, перезаписуємо
        contacts[name] = phone
        return "Contact updated."
    return "Error: Contact not found."                       # Якщо контакта немає, видає помилку

def show_phone(args, contacts):                              # Функція, що показує номер телефону за ім'ям
    if len(args) != 1:                                       # Тул лише один аргумент потрібен
        return "Error: Invalid format. Use 'phone [name]'."
    name = args[0]
    return contacts.get(name, "Error: Contact not found.")   # В результаті до імені підтягнеться телефон, або помилка, якщо імені немає в списку

def show_all(contacts):                                      # Функція, що видає вміст нашого словника з контактами
    if not contacts:
        return "No contacts found."                          # Якщо словник ще порожній
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

# Тепер створюємо головну функцію, яка буде викликати наші попередні функції
def main():
    contacts = {}                                            # Задаємо порожній словник для збереження контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:                     # Завершення роботи бота
            print("Good bye!")
            break
        elif command == "hello":                             # Відповідь на команду 'hello'
            print("How can I help you?")
        elif command == "add":                               # Додавання нового контакту
            print(add_contact(args, contacts))
        elif command == "change":                            # Зміна існуючого контакту
            print(change_contact(args, contacts))
        elif command == "phone":                             # Показати номер телефону за ім'ям
            print(show_phone(args, contacts))
        elif command == "all":                               # Показати всі контакти
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()