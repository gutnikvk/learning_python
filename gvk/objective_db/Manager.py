from gvk.objective_db.Person import Person


class Manager(Person):

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, Person.Job.MANAGER, pay)

    def increase_pay_by_percent(self, percent, bonus=0.1):
        Person.increase_pay_by_percent(self, percent + bonus)
