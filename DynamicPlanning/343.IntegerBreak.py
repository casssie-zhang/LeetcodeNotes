class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0 for i in range(n+1)]
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(1, i): # j  ranges from 1, i-1
                dp[i] = max(dp[i], max(j * (i-j), dp[i-j] * j))

        return dp[-1]
