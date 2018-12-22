import shelve
import os


def load():
    os.chdir('shelve_database')
    db = shelve.open('people-classes')
    for key in db:
        print(key, '=>\n ', db[key].__class__.__name__, vars(db[key]), '\n')
    db.close()
