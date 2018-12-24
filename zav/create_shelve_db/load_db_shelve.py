import shelve
import os

os.chdir('shelve_database')
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])

print('\n ', db['Sue']['name'])
db.close()