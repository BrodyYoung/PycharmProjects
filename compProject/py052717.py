with open('resrc/three.txt','w') as f1:
    f1.write('今天是周五,')


with open('resrc/three.txt','a') as f2:
    lst=['今天天津','是个','晴天']
    f2.writelines(lst)

with open('resrc/three.txt','r') as f3:
    print(f3.read(4))

with open('resrc/three.txt','r' ) as f4:
    f4.seek(6)
    print(f4.read())
    print(f4.tell())

# 文件复制
with open('resrc/123.jpg','rb') as i1:
    with open('resrc/101.jpg','wb') as i2:
        i2.write(i1.read())

