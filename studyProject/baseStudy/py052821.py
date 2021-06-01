# 获取指定目录下的全部py文件
import os

# 获取指定目录的所有文件

path = os.getcwd()
lst = os.listdir(path)
for i in lst:
    if i.endswith('.py'):
        print(i)




'''a = os.listdir('../baseStudy')
count = 0
for i in range(len(a)):
    if os.path.splitext(a[i])[1] == '.py':
        print(a[i])
        count += 1
print(count)'''
