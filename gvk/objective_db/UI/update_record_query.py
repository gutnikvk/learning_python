import shelve
from gvk.objective_db.Person import Person

db = shelve.open('../class_shelve')
while True:
    key = input('Enter the key, please => ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(
            None,
            None,
            None,
            None
        )
    field = input('Enter the field you would like to change => ')
    if not field: break
    if field in Person.__dir__(record):
        Person.__setattr__(record, field, input('Enter the value => '))