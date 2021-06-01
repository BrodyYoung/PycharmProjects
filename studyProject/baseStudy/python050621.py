class Student:
    # 类属性
    place = '河北'

    # 初始化方法（类似于JAVA中的构造函数）
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('我的名字叫', self.name, ',我今年', self.age, '岁了')

    def eat(self):
        print('我是',self.name,'今天吃了桃子')
    @classmethod
    def cm(cls):
        print('这是类方法')

    @staticmethod
    def sm():
        print('这是静态方法')


stu1 = Student('小杨', 24)
print(stu1.age)
print(stu1.name)
stu1.info()
stu1.eat()
print('------------------------------')
Student.eat(stu1)
print('------------------------------')
print(stu1.place)
Student.place='天津'
print(stu1.place)
print('------------------------------')
Student.sm()
Student.cm()



