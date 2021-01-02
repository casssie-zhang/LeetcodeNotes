
# -*- coding:UTF-8 -*-

def max_profit_one(a):
    """
    只允许买卖一次
    # 用 [公式] 表示第 [公式] 天的行为是”卖出“时，能得到的最大收益。
    # 显然，我们固定了卖出的时间，只要在这个时间点之前的时间中选择股票价格比最小的时候买入，就可以确定$dp[i]$的值。
    #
    # 所以我们可以遍历价格序列，
    # cur_min不断更新以记录当前时间点之前的股票最低价格，所以 [公式] ，
    # 最后所有dp[i]中的最大值就是只进行一次买卖能得到的最大利润。可以在求 [公式] 的同时用一个变量来记录其最大值。
    #
    # 因为 [公式] 只用到一次，所以没必要开一个数组专门来存储。
    :param a:
    :return:
    """
    cur_min = a[0]
    profit = 0
    for i in range(len(a)):
        profit = max(a[i] - cur_min, profit) #每个状态下减去当前的最小值 --  当前时间可获得的最大利润
        cur_min = min(a[i], cur_min)
    return profit

def max_profit_unlimited(a):
    """
    不限制买卖次数
    :param a:
    :return:
    """
    profit = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            continue
        else:
            profit += a[i+1] - a[i]
    return profit


def max_profit_two(a):
    """
    最多只能买卖两次
    :param a:
    :return:
    """
    profit = 0
    buy1 = buy2 = float('inf')
    pro1 = pro2 = 0
    for p in a:
        buy1 = min(buy1, p)
        pro1 = max(pro1, p-buy1)
        buy2 = min(buy2, p-pro1)
        pro2 = max(pro2, p-buy2)

if __name__ == '__main__':
    a = [3,5,7,3,8,1]
    print(max_profit_one(a))
    print(max_profit_unlimited(a))

