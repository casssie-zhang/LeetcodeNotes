class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                left = 0 if j == 0 else dp[i][j - 1]
                top = 0 if i == 0 else dp[i - 1][j]
                dp[i][j] = left + top

        return dp[-1][-1]

