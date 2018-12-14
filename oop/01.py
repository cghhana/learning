'''
定义一个学生类，形容学生
'''
# 定义一个空类
class Student():
    pass#直接跳过
# 定义一个对象：
cgh = Student()



# 定义一个类，用来描述其他学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'

    #1.函数的缩进层级！
    #2.系统默认一个self参数
    def Homework(self):
        print('doing homework')
        #在函数末尾使用return
        return None

#实例化对象
chenguanhua = PythonStudent()
print(chenguanhua.age)
print(chenguanhua.name)
chenguanhua.Homework()



