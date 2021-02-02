class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        j = n

        while(i<j):
            m = i + (j-i)//2
            curr = isBadVersion(m)
            prev = isBadVersion(m-1)
            if curr and prev:
                j = m - 1
            elif not curr and not prev:
                i = m + 1
            else:
                return m
        return i