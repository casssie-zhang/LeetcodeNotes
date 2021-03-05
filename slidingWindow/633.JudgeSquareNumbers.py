import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1:
            return True

        i, j = 0, int(math.sqrt(c))
        while(i<=j):
            res = i * i + j * j
            if res == c:
                return True
            elif res > c:
                j -= 1
            else:
                i += 1
        return False