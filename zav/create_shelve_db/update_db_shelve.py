from database import marina
import shelve
import os

os.chdir('shelve_database')
db = shelve.open('people-shelve')
sue = db['Sue']  # извлекает объект sue
sue['pay'] *= 1.50
db['sue'] = sue  # изменяет объект sue
db['Marina'] = marina  # добавляет новую запись
db.close()
