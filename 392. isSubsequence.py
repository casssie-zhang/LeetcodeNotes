#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 16:44
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == 0:
        return True

    i, j = 0, 0
    while ((i < len(s)) & (j < len(t))):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

def isSubsequence2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == 0:
        return True

    for char in s:
        try:
            index = t.index(char)
            t = t[index + 1:]
        except ValueError:
            return False
    return True

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))