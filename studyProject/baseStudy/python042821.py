'''
set集合
特点：无序、不能重复
'''
name={'jack','tome','king','tome','jackson'}
print(name)   #   {'jack', 'jackson', 'tome', 'king'}

print('jack' in name)

a=set("abcdefg")
b=set('efghijk')
# a有，b没有
print(a-b)     # abcd
#并集

print(a|b)
#交集
print(a&b)
#
print()






