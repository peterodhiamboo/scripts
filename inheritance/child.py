from people import Person

class my_child(Person):
    pass

child = my_child('Jane', 'Doe', 12)
print(child.instance_number)
child_1 = my_child('Diana', 'Stone', 15)
print(child_1.instance_number)