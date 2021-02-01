class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x

        self.x = x
        return self.search(1, x)

    def search(self, l, r):
        # print("l, r:", l, r)
        if r - l <= 1:
            return l
        mid = (l + r) // 2
        if mid * mid == self.x:
            return mid
        if mid * mid < self.x:
            return self.search(mid, r)
        else:
            return self.search(l, mid)