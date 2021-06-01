with open('C:\\Users\\Young\\Desktop\\demo101.txt', 'w') as f1:
    f1.write('奋斗成就更好的你')

f2 = open('C:\\Users\\Young\\Desktop\\demo102.txt', 'w')
print('奋斗成就更好的你', file=f2)
f2.close()
