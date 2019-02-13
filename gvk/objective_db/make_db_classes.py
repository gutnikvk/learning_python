import shelve
from gvk.objective_db.Person import Person
from gvk.objective_db.Manager import Manager

bob = Person(
    name='Bob Smith',
    age=42,
    pay=3000,
    job='Middle developer'
)

sue = Person(
    name='Sue Jones',
    age=30,
    pay=1000,
    job='Junior developer'
)

tom = Manager(
    name='Tom Doe',
    age=50,
    pay=5000
)

db = shelve.open('class_shelve')
db['Bob'] = bob
db['Sue'] = sue
db['Tom'] = tom
db.close()
