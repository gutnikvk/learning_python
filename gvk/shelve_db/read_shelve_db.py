import shelve

db = shelve.open('shelve-people')
for key in db:
    print(key, '=>', db[key])
print(db['Sue']['name'])
db.close()