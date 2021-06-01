# 读
f1=open('resrc/one.txt', 'r')
# print(f1.read(3))
# print('------------------')
# print(f1.readline())
print(f1.readlines())
f1.close()

# 写
f2=open('resrc/three.txt', 'w')
f2.write('今天是周四，')
sList=['今天','天津','风','很大']
f2.writelines(sList)
f2.close()

# seek
f3=open('resrc/three.txt', 'r')
f3.seek(12)
print(f3.read())
print(f3.tell())
f3.close()

# with
with open('resrc/three.txt', 'r') as file:
    print(file.read())

# with 实现文件复制
with open('resrc/img/nezha.jpg', 'rb') as j1:
    with open('resrc/img/nez.jpg', 'wb') as j2:
        j2.write(j1.read())

