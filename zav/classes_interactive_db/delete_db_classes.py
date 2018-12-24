import shelve
import os


def delete():
    os.chdir('shelve_database')
    while True:
        print('Какую запись хотите удалить? Введите полное имя сотрудника:')
        name = input()
        print('Вы удаляете ' + name + '. Вы уверены? Нажмите y или n')
        choice = input()
        if choice == 'y':
            db = shelve.open('people-classes')
            try:
                del db[name]
                print(name + ' Успешно удален.')
                db.close()
            except KeyError:
                print('Неверная запись')

        print('Вы хотите удалить другую запись? Нажмите y или n')
        choice = input()
        if choice == 'y':
            continue
        else:
            break
