# 只写模式
f1 = open('./resrc/one.txt', 'w')
f1.write('中华')
f1.close()

# 只读模式
f2 = open('./resrc/one.txt', 'r')
print(f2.readlines())
f2.close()

# 追加模式
f3 = open('./resrc/one.txt', 'a')
f3.write('\n人民')
f3.close()

# 二进制模式
sFile = open('./resrc/123.jpg', 'rb')
tFile = open('./resrc/sea.jpg', 'wb')
tFile.write(sFile.read())
tFile.close()
sFile.close()

# 读写模式
f5 = open('./resrc/one.txt', 'r+')
f5.write('\n共和国')
print(f5.readline())
f5.close()

# 以二进制的方式读图片
f7=open('./resrc/123.jpg','rb')
print(f7.read())
f7.close()

#
f6=open('./resrc/two.txt','r')
# print(f6.read())
print('---------------------------')
print(f6.readline())
print('---------------------------')
print(f6.readlines())
# print('---------------------------')
f6.close()





