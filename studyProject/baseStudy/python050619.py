name = '小杨'


def fun():
    age = 35
    global score
    score = 98
    print(name, age, score)


fun()
print(score)
print('------------------')


def func(a):
    if a == 1:
        return 1
    else:
        return a * func(a - 1)


print(func(5))
