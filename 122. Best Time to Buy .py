#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 15:52
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
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
