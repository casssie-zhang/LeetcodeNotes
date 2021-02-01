#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/8 14:45
# @Author : 10029
# @Email: zhangkexin@zhoupudata.com

# can use `recursion` or `dynamic planning
def diffWaysToCompute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    operators_dict = {
        "-": lambda x, y: x-y,
        "+":lambda x, y: x + y,
        "*":lambda x, y:x * y
    }
    def helper(lb, rb):
        '''
        helper
        :param lb:
        :param rb:
        :return:
        '''
        ans = []
        for i in range(lb, rb):
            if input[i] not in operators_dict:
                continue
            # if input[i] is a operator.
            # then do operation on the left and right side of input[i] using input[i]
            ans += [operators_dict[input[i]](le, ri) for le in helper(lb,i)
                    for ri in helper(i+1,rb)]
        # when lb = rb+1. which means we only have a number. --> there is no operator in this string
        # return the int directly
        return ans if len(ans)!=0 else [int(input[lb:rb])]

    return helper(0, len(input))



if __name__ == '__main__':
    input = "2*3-4*5"
    print(diffWaysToCompute(input))
