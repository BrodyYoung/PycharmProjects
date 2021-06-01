import os

path = os.getcwd()
list_files = os.walk(path)
for dirpath, dirname, filename in list_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('------------------------')
