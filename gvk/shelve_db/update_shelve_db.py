import shelve

db = shelve.open('shelve_people')
db['Sue']['pay'] += 1000

jack = {
    'name': 'Jack Daniels',
    'age': 80,
    'job': 'whiskey distiller',
    'pay': 8000
}
db['Jack'] = jack

db.close()