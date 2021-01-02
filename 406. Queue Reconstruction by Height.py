#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/5 15:36
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    # 个子高的人先插入
    # 个子矮的人插入前面 不会影响第二个数值
    output = []
    sorted_people = sorted(people, key=lambda x: (x[0], -x[1]))
    while sorted_people:
        curr_people = sorted_people.pop()
        output.insert(curr_people[1], curr_people)

    return output


if __name__ == '__main__':
    input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    print(reconstructQueue(input))

