import shelve
from Person import Person
from Manager import Manager
from Urbanist import Urbanist
import os
import pathlib

pathlib.Path('shelve_database').mkdir(exist_ok=True)
os.chdir('shelve_database')

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)
marina = Urbanist('Marina Dadakhanova', 20, 500000)
workers = {bob, sue, tom, marina}

db = shelve.open('people-classes')
for person in workers:
    db[person.name] = person
db.close()
