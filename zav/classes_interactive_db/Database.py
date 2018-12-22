import load_db_classes
import update_db_classes
import delete_db_classes
import new_db_classes
import os
cwd = os.getcwd()

print('Привет! Это программа для работы с базой данных. Вот, что ты можешь сделать: ')
while True:
    os.chdir(cwd)
    print('1. Распечатать базу данных \n'
          '2. Добавить запись \n'
          '3. Изменить запись \n'
          '4. Удалить запись \n'
          '5. Выйти')
    _ = int(input())
    if _ == 1:
        load_db_classes.load()
    elif _ == 2:
        new_db_classes.new()
    elif _ == 3:
        update_db_classes.update()
    elif _ == 4:
        delete_db_classes.delete()
    elif _ == 5:
        break
    else:
        print('Неверное значение')



