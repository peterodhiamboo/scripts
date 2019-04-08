from people import Person

class Worker(Person):
    def __init__(self, fname, lname, age, profession):
        super().__init__(fname, lname, age)
        self.profession = profession

worker_1 = Worker('Sylviah', 'Muli', 35, 'Engineer')