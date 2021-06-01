import os.path

print(os.path.abspath('resrc/img/nezha.jpg'))  # E:\AProject\PycharmProjects\pythonProject\study\baseStudy\nezha.jpg
print(os.path.exists('resrc/img/nezha.jpg'))  # true

print(os.path.join('C:\\Users\\Young\\Desktop', 'Java简历'))  # C:\Users\Young\Desktop\Java简历
print(os.path.split('C:\\Users\\Young\\Desktop\\Java简历'))   # ('C:\\Users\\Young\\Desktop', 'Java简历')

print(os.path.splitext('calc2.py'))  # ('calc2', '.py')

print(os.path.basename('C:\\Users\\Young\\Desktop\\Java简历'))  # Java简历
print(os.path.dirname('C:\\Users\\Young\\Desktop\\Java简历'))  # C:\Users\Young\Desktop
print(os.path.isdir('resrc/img/nezha.jpg'))   # False
print(os.path.isdir('C:\\Users\\Young\\Desktop\\Java简历'))   # True
