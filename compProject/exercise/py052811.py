# 需求: 企业发放的奖金根据利润提成。从键盘输入当月利润I，求应发放奖金总数？
# 利润(i)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%
# 高于100万元时，超过100万元的部分按1%提成

print('---------------------------')
profit = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0
i = int(input('请输入您的利润：'))
for j in range(6):
    if i > profit[j]:
        bonus += (i - profit[j]) * rate[j]  # 减去基本数 再计算奖金
        i = profit[j]  # 下次计算的利润值
print(bonus)
print('----------------------')
ip = input('请输入当月利润:')
i = int(ip)
if i <= 10:
    print('您的奖金是：', 0.1 * i)
elif i > 10 and i < 20:
    s = 10 * 0.1 + (i - 10) * 0.075
    print('您的奖金是：', s)
elif i > 20 and i < 40:
    s = 10 * 0.1 + 10 * 0.075 + (i - 20) * 0.05
    print('您的奖金是：', s)
elif i > 40 and i < 60:
    s = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (i - 40) * 0.03
    print('您的奖金是：', s)
elif i > 60 and i < 100:
    s = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (i - 60) * 0.015
    print('您的奖金是：', s)
elif i > 100:
    s = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (i - 100) * 0.01
    print('您的奖金是：', s)
