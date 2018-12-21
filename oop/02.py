'''
class A():
    name = 'cgh'
    age = '21'

    def __init__(self):
        self.name = 'cgh1'
        self.age = '20'
    def student(self):
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))
class B():
    name = 'cgh2'
    age = '19'

a = A()
print(id(a))
a.student()
A.student(a)
A.student(A)
A.student(B)
'''
class person():
    name = 'cgh'
    __age='18'
c = person()
print(c.name)
print(c._person__age)



