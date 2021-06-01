import pack1.moduleA as ma
from pack1 import moduleA as ba
from pack1.moduleA import add 

print(ma.add(10, 80))
print(ba.add(10, 90))
print(add(2,8))
