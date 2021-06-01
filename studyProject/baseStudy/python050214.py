# 数据类型转换

num1 = 1
str1 = '10'
z1 = str(num1)
print(z1)  # 1
print(type(z1))  # str

z2 = float(str1)
print(z2)  # 10.0
print(type(z2))  # float

list1 = [10, 20, 30]
tu1 = tuple(list1)
print(tu1)
print(type(tu1))

z4 = set(list1)
print(z4)  #
print(type(z4))  #

t1 = (100, 200, 300)

str2 = '1'
str3 = '1.1'
str4 = '(1000,2000,3000)'
str5 = '[100,200,300]'
z5 = eval(str2)
print(z5)
print(type(z5))

z6 = eval(str3)
print(z6)
print(type(z6))

z7 = eval(str4)
print(z7)
print(type(z7))
