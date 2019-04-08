from child import child, child_1
from professional import worker_1

def printer():
    for name in (child, child_1, worker_1):
        print(name.fullname())
        print(name.instance_number)
        print('')


printer()
