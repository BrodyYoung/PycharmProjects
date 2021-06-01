# 只读模式 r
fil=open('resrc/one.txt', 'r')
print(fil.readlines())
fil.close()

# 只写模式 w
file2=open('resrc/two.txt', 'w')
file2.write('中华')
file2.close()

# 追加模式 a
f3=open('resrc/two.txt', 'a')
f3.write('\n人民')
f3.close()

# 二进制模式 b
srcFile=open('resrc/img/nezha.jpg', 'br')
targetFile=open('resrc/img/newNezha.jpg', 'bw')
targetFile.write(srcFile.read())

targetFile.close()
srcFile.close()

# 读写模式
f4=open('resrc/two.txt', 'a+')
print(f4.readlines())
f4.write('共和国')
f4.close()
