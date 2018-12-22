import shelve
import os


def update():
    os.chdir('shelve_database')
    db = shelve.open('people-classes')
    while True:
        print('Какую запись хотите изменить? Введите полное имя сотрудника:')
        name = input()
        try:
            rec = db[name]
            print('Введите имя атрибута для изменения или добавьте свой: ')
            print(name, vars(db[name]))
            attr = input()
            print('Введите новое значение атрибута или "delete" для его удаления: ')
            new_value = input()
            if new_value == 'delete':
                print('Вы уверены, что хотите удалить атрибут ' + attr + '? Нажмите y или n')
                choice = input()
                if choice == 'y':
                    delattr(rec, attr)
                    print(attr + ' успешно удален.')
                    db[name] = rec
            else:
                setattr(rec, attr, new_value)
                print(attr + ' успешно изменен.')
                db[name] = rec
        except KeyError:
            print('Неверная запись')

        print('Вы хотите изменить другую запись? Нажмите y или n')
        choice = input()
        if choice == 'y':
            continue
        else:
            break

