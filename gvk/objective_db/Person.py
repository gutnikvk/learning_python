class Person:
    name: str
    age: int
    job: object
    pay: float

    def __init__(self, name, age, job, pay):
        self.__name = name
        self.__age = age
        self.__job = job
        self.__pay = pay

    def __str__(self):
        return self.__class__.__name__ + ' => ' + self.name + ', ' + str(self.age) + 'yo: ' + str(self.pay) + ', ' + str(self.job)

    def get_last_name(self):
        return self.name.split()[-1]

    def get_first_name(self):
        return self.name.split()[0]

    def get_full_name(self):
        return self.name

    def get_pay(self):
        return self.pay

    def get_job(self):
        return self.job

    def get_age(self):
        return  self.age

    def set_pay(self, new_pay):
        self.pay = new_pay

    def increase_pay_by_number(self, change_amount):
        self.pay += change_amount

    def decrease_pay_by_number(self, change_amount):
        self.pay -= change_amount

    def increase_pay_by_percent(self, percent):
        self.__pay *= (1 + percent / 100)

    def decrease_pay_by_percent(self, percent):
        self.pay *= (1 - percent / 100)
