#!/usr/bin/env python
# -*- coding: utf-8 -*-


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # complete as many as transactions as you like
    # must sell before buy
    # 对于[a, b, c, d]，如果有a <= b <= c <= d ，那么最大收益为d - a。而
    # d - a = (d - c) + (c - b) + (b - a) ，因此当访问到一个prices[i]
    # 且prices[i] - prices[i - 1] > 0，那么就把prices[i] - prices[i - 1]添加到收益中。
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit



if __name__ == '__main__':
    input = [1,2,3,4,5]
    print(maxProfit(input))
    input = [7,1,5,3,6,4]
    print(maxProfit(input))
