import model


def main_menu():
    print('\nГлавное меню.')
    menu_list = ['Открыть файл',
                 'Показать все контакты',
                 'Добавить контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Найти контакт',
                 'Сохранить файл',
                 'Выход\n'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    while True:
        user_input = input('Выбери пункт: ')
        if user_input.isdigit():
            if 0 < int(user_input) < 9:
                return int(user_input)
            else:
                print('Введите число от 1 до 8.')
        else:
            print('Введите число от 1 до 8.')



def show_db(db):
    if db_success(db):
        for i in range(len(db)):
            print(f'\t{i + 1}.', end=' ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db and not model.count:
        model.count = 1
        print('Телефонная книга открыта.')
        return True
    elif db and model.count:
        return True
    else:
        print('Телефонная книга не открыта или пуста.')
        return False


def exit_programm(start_db, finish_db):
    if db_success(finish_db):
        if start_db == finish_db:
            print('Завершение программы.')
            exit()
        else:
            print('Данные изменены. Хотите ли вы их сохранить?')
            save_choice = input('Для выхода и сохранения изменений нажимите "1" или без сохранения - любую кнопку: ')
            return save_choice
    else:
        print('Завершение программы.')
        exit()




def create_contact():
    if db_success(model.db_list):
        print('Создание нового контакта.')
        new_contact = dict()
        new_contact['lastname'] = input('Введите фамилию: ')
        new_contact['firstname'] = input('Введите имя: ')
        new_contact['phone'] = input('Введите телефон: ')
        new_contact['comment'] = input('Введите комментарий: ')
        return new_contact


def search_contact(db):
    if db_success(db):
        search = input('Введите информормацию для поиска нужного контакта: ')
        if db_success(db):
            quantity = 0
            for i in range(len(db)):
                if search in db[i].values():
                    print(f'\t{i + 1}.', end=' ')
                    for v in db[i].values():
                        print(f'{v}', end=' ')
                    quantity += 1
                    print()
            if quantity:
                print(f'Колличество найденых контактов - {quantity}.')
                return True
            else:
                print('Контакт не найден.')
                return False


def change_contact(db):
    if search_contact(db):
        change_ID = int(input('Введите номер(ID) контакта для изменения: '))
        change_contact = dict()
        change_contact['lastname'] = input('Введите фамилию: ')
        change_contact['firstname'] = input('Введите имя: ')
        change_contact['phone'] = input('Введите телефон: ')
        change_contact['comment'] = input('Введите комментарий: ')
        return change_contact, change_ID
    else:
        return 0, 0


def delete_contact(db):
    if search_contact(db):
        delete = int(input('Введите номер(ID) контакта для удаления: '))
        return delete


