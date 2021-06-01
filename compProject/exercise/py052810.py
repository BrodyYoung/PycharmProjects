# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0
for g in range(1, 5):
    for s in range(1, 5):
        for b in range(1, 5):
            if g != s and s != b and g != b:
                n = 100 * b + 108 * s + g
                print(n)
                count += 1

print(count)
