# 两个变量的交换
a = 20
b = 30
print(f"变量交换之前a的值为{a},b的值为{b}")
# 第一种方式：使用临时变量
temp=a
a=b
b=temp
print(f"变量交换之后a的值为{a},b的值为{b}")

# 第二种方式：python特有的方式
a,b=b,a
print(f"变量交换之后a的值为{a},b的值为{b}")





