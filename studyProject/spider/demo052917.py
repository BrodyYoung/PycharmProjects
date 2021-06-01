import re

print('--------------字符-----------------')
r1 = re.findall('abc', 'abcavc')
print(r1)        # abc

r2 = re.findall('a.c', 'abcdapc')
print(r2)        # abc    apc

r3 = re.findall('a.c', 'a\ncd')
print(r3)        #

r3 = re.findall('a\.c', 'a.cabc')
print(r3)        # a.c

r4 = re.findall('a[bcd]e', 'aceade')
print(r4)        # ace   ade

print('--------------预定义字符-----------------')
r = re.findall('a\db', 'ta5btaubtabt')
print(r)        # a5b

r = re.findall('a\Db', 'ta5btaubtabt')
print(r)        # aub

r = re.findall('a\sb', 'ta btavbtabt')
print(r)        # a b

r = re.findall('a\Sb', 'ta btavbtabt')
print(r)        # avb

r = re.findall('a\wb', 'taTbtarbta9bta bta中bta%b')
print(r)        # aTb   arb   a9b  a中b

r = re.findall('a\Wb', 'taTbtarbta9bta bta中bta%b')
print(r)        # a b  a%b

print('--------------数量词-----------------')
r = re.findall('abc*', 'tabtabccct')
print(r)        # ab    abccc

r = re.findall('a\d*', 'ta123tat')
print(r)        # ab    abccc

r = re.findall('abc+', 'tabtabctabccct')
print(r)        # a123   a

r = re.findall('abc?', 'ttabttabctabccct')
print(r)        # ab   abc   abc

r = re.findall('abc{2}', 'tabctabcctabccctt')
print(r)        # abcc   abcc