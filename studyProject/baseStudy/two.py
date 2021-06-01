age = 18
name = 'Tom'
weight = 61.5
stu_id = 1

print('我的年龄是%d岁' % age)

print('我的名字是%s' % name)

print('我的体重是%f公斤' % weight)

print('我的体重是%.2f公斤' % weight)

print('我的学号是%d' % stu_id)

print('我的学号是%03d' % stu_id)

print('我的名字是%s，今年%d岁了' % (name, age))

print('我的名字是%s，明年%d岁' % (name, age + 1))

print('我的名字是%s，我今年%d岁了，我的体重是%.2f公斤，我的学号是%06.d' % (name, age, weight, stu_id))

print(f'我的名字是{name}，今年{age}岁了，体重是{weight}公斤')
