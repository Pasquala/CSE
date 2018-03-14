class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print('%s goes to work' % self.name)


class Employee(Person):
    def __init__(self, name, age, working):
        super(Employee, self).__init__(name, age)
        self.employed = working

    def is_employed(self):
        if self.employed:
            print('%s is indeed employed!' % self.name)
        elif not self.employed:
            print('%s must have been fired...' % self.name)


class Programmer(Employee):
    def __init__(self, name, age, working, programming):
        super(Programmer, self).__init__(name, age, working)
        self.programming = programming

    def program(self):
        if self.programming:
            print('%s is busy coding away, its probably best to not bother him.' % self.name)
        elif not self.programming:
            print('%s was not coding? They must of been taking a lunch break.' % self.name)
            self.programming = True


potato = Programmer('Jeef', 21, True, False)
potato.work()
potato.is_employed()
potato.program()
potato.program()