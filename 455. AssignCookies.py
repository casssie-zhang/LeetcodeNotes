#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/3 16:42
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if (not g) or (not s):
            return 0
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        happy = 0
        i, j = 0, 0
        while((i<len(sorted_g)) & (j<len(sorted_s))):
            if sorted_g[i] <= sorted_s[j]:
                happy += 1
                i += 1 # this child is satisfied, i++
            j += 1

        return happy


if __name__ == '__main__':
    ss = Solution()
    children_content, cookie_size = [1, 2, 3], [1,1]
    print(ss.findContentChildren(children_content, cookie_size))