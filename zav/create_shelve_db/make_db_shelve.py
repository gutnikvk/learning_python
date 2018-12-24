from database import bob, sue, tom, kek
import shelve
import os
import pathlib

pathlib.Path('shelve_database').mkdir(exist_ok=True)
os.chdir('shelve_database')
db = shelve.open('people-shelve')
db['Bob'] = bob
db['Sue'] = sue
db['Tom'] = tom
db['Kek'] = kek
db.close()
