from gvk.objective_db.Person import Person as Person
from gvk.objective_db.Manager import Manager as Manager

tom = Manager(
    name='Tom Smith',
    age=42,
    pay=3000
)

john = Person(
    name='John Jones',
    age=30,
    job='Junior developer',
    pay=1000
)

print(tom)
print(john)
