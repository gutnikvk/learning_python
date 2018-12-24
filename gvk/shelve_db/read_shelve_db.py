import shelve

db = shelve.open('shelve_people')
for key in db:
    print(key, '=>', db[key])
db.close()