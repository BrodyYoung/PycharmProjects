# m = 1000
# q = int(input('请输入想取得钱数：'))
# if m >= q:
#     m = m - q
#     print('取款成功,账户余额是%d' % m)
# else:
#     print('取款失败，账户余额是%d' % m)
# print("-----------------------------------------")
# sc = int(input('请输入你的成绩：'))
# if sc > 90:
#     print('A')
# elif sc > 80:
#     print('B')
# elif sc > 80:
#     print('C')
# elif sc > 70:
#     print('D')
# elif sc > 60:
#     print('E')
# else:
#     print('F')
# print("-----------------------------------------")
# i = input('您是会员吗？')
# m = int(input('您的购物金额是多少？'))
# if i == 'Y':
#     if m >= 200:
#         print(f'您总共消费{0.8 * m}元')
#     elif m >= 100:
#         print(f'您总共消费{0.9 * m}元')
#     else:
#         print(f'您总共消费{m}元')
# else:
#     if m >= 200:
#         print(f'您总共消费{0.95 * m}元')
#     else:
#         print(f'您总共消费{m}元')

a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
print('a大于b' if a > b else 'a小于等于b')
