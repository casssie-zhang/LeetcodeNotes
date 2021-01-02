#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/3 17:21
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        s_intervals = sorted(intervals, key=lambda x: x[1])
        rmv_num = 0
        i = 1
        end = s_intervals[0][1]
        while i<len(s_intervals):
            if end <= s_intervals[i][0]:
                end = s_intervals[i][1]
            else:
                rmv_num += 1
            i += 1
        return rmv_num




if __name__ == '__main__':
    input = [[1,100],[11,22],[1,11],[2,12]]
    s = Solution()
    print(s.eraseOverlapIntervals(input))