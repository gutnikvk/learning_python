from Person import Person


class Manager(Person):  # ссылаемся на родителя
    def give_raise(self, percent, bonus=0.1):  # меняем метод give_raise из родителя
        Person.give_raise(self, percent/100 + bonus)

    def __init__(self, name=None, age=None, pay=0):  # добавляем значение атрибута job
        Person.__init__(self, name, age, pay, 'manager')

    def __str__(self):  # меняем строчный вывод объекта
        i = 1
        for key in self.__dict__:
            print('attribute%d: ' % i, key)  # выводим имена атрибутов
            i += 1
        return '<%s => %s>' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)
    print(tom)
    print(tom.__dict__)

# instance.method(arg1, arg2) -> объект.метод(аргументы) (ищет метод в импортированных классах)
# class.method(instance, arg1, arg2) -> класс.его метод (объект(можно self), аргументы)
