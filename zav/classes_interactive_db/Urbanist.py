from Person import Person


class Urbanist(Person):
    def __init__(self, name=None, age=None, pay=0):
        Person.__init__(self, name, age, pay, 'urbanist')

    def give_raise(self, percent, bonus=0.2):
        Person.give_raise(self, percent/100 + bonus)
