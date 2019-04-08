class Person:
    instance_number = 0
    def __init__(self, fname, lastname, age):
        self.fname = fname
        self.lastname = lastname
        self.age = age

        Person.instance_number += 1

    def age_name(self):
        if self.age < 18:
            return f'You are not yet an adult, wait for {18 - self.age} year/s'
        else:
            return f'You are considered an adult, pay your taxes and live free'

    def fullname(self):
        return f'{self.fname} {self.lastname}'
