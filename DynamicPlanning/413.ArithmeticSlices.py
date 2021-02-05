class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # dp[2] = 1
        #     [0, 1, 2]
        #
        # dp[3] = dp[2] + 1 = 2
        #     [0, 1, 2, 3], // [0, 1, 2] 之后加一个3
        #     [1, 2, 3] // 新的递增子区间
        #
        #
        # dp[4] = dp[3] + 1 = 3
        #     [0, 1, 2, 3, 4], // [0, 1, 2, 3]之后加一个4
        #     [1, 2, 3, 4], // [1, 2, 3]之后加一个4
        #     [2, 3, 4] // 新的递增子区间

        if len(A) <= 2: return 0
        dp = [0 for i in range(len(A))]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1

        return sum(dp)