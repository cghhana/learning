#Mixin案例
class Person():
    name = 'cgh'
    age = 18
    def Eat(self):
        print('eating')
    def Drink(self):
        print('drinking')
    def sleep(self):
        print('sleeping')
class Teacher(Person):
    def work(self):
        print('working')
class Student():
    def study(self):
        print('studing')

class Tutor(Teacher,Student):
    pass
t = Tutor
print(Tutor.__mro__)






