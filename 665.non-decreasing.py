#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 17:12
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 在出现nums[i] < nums[i - 1]时，需要考虑的是应该修改数组的哪个数，使得本次修改能使
    # i之前的数组成为非递减数组，并且不影响后续的操作 。优先考虑令nums[i - 1] = nums[i]，
    # 因为如果修改nums[i] = nums[i - 1]的话，那么nums[i]这个数会变大，就有可能比nums[i + 1]
    # 大，从而影响了后续操作。

    # 还有一个比较特别的情况就是nums[i] < nums[i - 2]，修改nums[i - 1] = nums[i]
    # 不能使数组成为非递减数组，只能修改nums[i] = nums[i - 1]。
    i = 0
    change_flag = False
    while (i < len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if not change_flag:
                change_flag = True
                pos = i
            else:
                return False
        i += 1
    # there are two options:(1)lower nums[i] if nums[i+1]>=nums[i-1]
    # (2)increase nums[i+1] if nums[i] <= nums[i+2]
    if not change_flag:
        return True
    if (pos == len(nums) - 2) or pos == 0:
        return True
    elif nums[pos - 1] <= nums[pos + 1] or nums[pos] <= nums[pos + 2]:
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [4, 2, 3]
    print(checkPossibility(nums))