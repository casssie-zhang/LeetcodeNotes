#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 16:21
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    possible_flowers = 0
    continue_zero_cnt = 0
    flowerbed = [0] + flowerbed + [0]
    for flower in flowerbed:
        if flower == 1:
            possible_flowers += (continue_zero_cnt-1) // 2
            continue_zero_cnt = 0
        else:
            continue_zero_cnt += 1
    possible_flowers += (continue_zero_cnt - 1) // 2
    if possible_flowers >= n:
        return True
    else:
        return False


if __name__ == '__main__':
    flowerbed = [0, 0, 1, 0, 0]
    n = 2
    print(canPlaceFlowers(flowerbed, n))