#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/3 15:49
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    common = []
    words_num = len(strs)
    for i in range(len(strs[0])):
        a = strs[0][i]
        flag=True
        for j in range(1,words_num):
            try:
                if a != strs[j][i]:
                    flag=False
                    break
            except:
                break
        if flag==True:
            common.append(a)
        else:
            break
    return "".join(common)

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))