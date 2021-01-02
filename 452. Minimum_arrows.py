#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/3 17:44
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if not points:
        return 0
    sorted_points = sorted(points,key=lambda x: x[1])
    overlap_group = 1
    end = sorted_points[0][1]
    i = 1
    while(i<len(sorted_points)):
        s = sorted_points[i][0]
        if end < sorted_points[i][0]: # 如果不重叠
            overlap_group += 1 # next elements' right bound
            end = sorted_points[i][1]
        i += 1
    return overlap_group


if __name__ == '__main__':
    input = [[10,16], [2,8], [1,6], [7,12]]
    print(findMinArrowShots(input))