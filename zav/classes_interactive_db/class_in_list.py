from Person import Person
bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)
people = [bob, sue]
for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people]
print('\n', x)
print('\n', [rec.name for rec in people if rec.age >= 45])
print('\n', [(rec.age ** 2 if rec.age >= 45 else rec.age) for rec in people])


