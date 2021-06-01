import os

# os.system('notepad.exe')
# os.system('calc.exe')
# os.startfile('D:\\腾讯\\QQ\\Bin\\qq.exe')
os.startfile('C:\\Users\\Young\\Desktop\\123.txt')

print(os.getcwd())
# os.mkdir('newDir')
# os.makedirs('a/b/c')
# os.makedirs('f\g\e')

# os.rmdir('newDir')
# os.removedirs('a\\b\\c')

# os.chdir('E:\AProject\PycharmProjects\pythonProject\study\pack1')
os.chdir('../pack1')
print(os.getcwd())