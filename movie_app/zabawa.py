from datetime import datetime


def cos():
    print('cos')
    return datetime.now()

class A:
    x = cos()

    def __init__(self):
        print('ptyś')


a = A()
b = A()
c = A()
print(a.x)
print(b.x)
print(c.x)