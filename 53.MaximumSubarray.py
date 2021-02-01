#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 18:02
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def maxSubarray(nums):
    # max sum = itself = (1) value at index itself (2) previndex to currindex
    max_curr = nums[0]
    max_gbl = nums[0]
    i=1
    while(i<len(nums)):
        max_curr = max(nums[i], max_curr+nums[i])
        max_gbl = max(max_curr, max_gbl)
        i += 1
    return max_gbl

def maxSubarray1(nums):
    max_sum = 0
    max_ending_here = 0

    for i in nums:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0

        if max_ending_here > max_sum:
            max_sum = max_ending_here

    return max_sum if max_sum != 0 else max(nums)
if __name__ == '__main__':
    input = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubarray1(input))