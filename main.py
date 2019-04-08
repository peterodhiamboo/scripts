class Student:
    no_of_instances = 0

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


        Student.no_of_instances += 1

    def email_address(self):
        return f'{self.fname.lower()}{self.lname.lower()}@company.co.ke'

student_1 = Student('Peter', 'Odhiambo')
student_2 = Student('Mark', 'Wailer')
