# Задача №55.  Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input ('Введите Ф.И.О.: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: list[str], info: str) -> list[str] | str:
    """Находит в списке записи по определенному критерию поиска"""
    result = [contact for contact in book if info in contact]
    if not result:
        return 'Совпадений не найдено'
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('-----------------------')
        print('\n'.join(result))
        new_info = input('Введите данные для уточнения: ')
        return search(result, new_info)
    # book = book.split('\n')
    # return list(filter(lambda contact: info.lower() in contact.lower(), book))


def change_data() -> None:
    """Изменяет данные в справочнике."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_edit = input('Введите данные для изменения ')
    data_to_edit = search(data, data_to_edit)
    print(f'Выбранный контакт: {data_to_edit}')
    mode = input('Удалить или изменить? 1 - удаление, 2 - изменение, 3 - отмена ')
    if mode == '1':
        data.remove(data_to_edit)
    elif mode == '2':
        data[data.index(data_to_edit)] = enter_contact()
    elif mode == '3':
        return

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def enter_contact(contact: str) -> str:
    new_fio = input ('Введите Ф.И.О.: ')
    new_phone = input('Введите номер телефона: ')
    
    old_fio = contact.split(" | ")[0]
    old_phone = contact.split(" | ")[1]
    
    if len(new_fio) > 0 and len(new_phone) > 0:
        return f'\n{new_fio} | {new_phone}'
    elif not new_phone and len(new_fio) > 0:
        return f'\n{new_fio} | {old_phone}'
    elif not new_fio and len(new_phone) > 0:
        return f'\n{old_fio} | {old_phone}'


while True:
    print('1. вывод, 2. добавить, 3. поиск, 4. расширенный поиск, 5. измененить')
    mode = int(input())
    if mode == 1:
        show_data()
    elif mode == 2:
        add_data()
    elif mode == 3:
        find_data()
    elif mode == 4:
        search()
    elif mode == 5:
        change_data()
    else:
        break