def fun(a, b=10):
    print(a, b)


a = 100
print(fun(a))
print('-------------------')
# 个数可变的形参

# 个数可变的位置形参
def fun1(*args):
    print(args)


fun1(10)
fun1(10, 20, 30)
lst=[10,20,30]
fun1(*lst)

# 个数可变的关键字形参
def fun2(**args):
    print(args)
fun2(a=10,b=100)

# def fun3(*args1,*args2):
#     pass

# def fun4(**args1,**args2):
#     pass

# def fun5(**args1,*args2):
#     pass

def fun6(*args1,**args2):
    pass
