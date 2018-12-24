import shelve
import os
import Person
import Manager
import Urbanist


def new():
    os.chdir('shelve_database')
    db = shelve.open('people-classes')
    while True:
        print('Введите имя и фамилию нового сотрудника:')
        name = input()
        while True:  # цикл для неверной должности
            print('Введите должность сотрудника: ')
            print('Person\nManager\nUrbanist')
            input_class = input()
            if input_class == 'person' or input_class == 'Person':
                rec = Person.Person()
                break
            elif input_class == 'manager' or input_class == 'Manager':
                rec = Manager.Manager()
                break
            elif input_class == 'urbanist' or input_class == 'Urbanist':
                rec = Urbanist.Urbanist()
                break
            else:
                print('Неверная должность')

        rec.name = name
        blacklist = ['name']
        if rec.job is not None:
            blacklist.append('job')
        print('Заполним: ')
        for key in rec.__dict__:
            if key not in blacklist:
                print(key + ' = ')
                new_value = input()
                setattr(rec, key, new_value)

        db[name] = rec
        print('Запись ' + rec.name + ' успешно добавлена')
        print('Вы хотите добавить другую запись? Нажмите y или n')
        choice = input()
        if choice == 'y':
            continue
        else:
            break
