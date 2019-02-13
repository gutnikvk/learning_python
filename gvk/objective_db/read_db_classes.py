import shelve

db = shelve.open('class_shelve')
for key in db:
    print(key, ' => ', db[key].get_full_name(), db[key].get_pay())

bob = db['Bob']
print(bob.get_last_name())
