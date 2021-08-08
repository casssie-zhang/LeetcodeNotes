class Solution:
    def numTrees(self, n: int) -> int:
        # solution1: DP
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):  # n=3
            # i=3
            for j in range(i):  # 0 1 2
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]
        # solution2: dkw
#         self.mem = {0:1, 1:1, 2:2}
#         return self.consecutive_combo(n)

#     def consecutive_combo(self, n):
#         if n <= 2:
#             return n

#         if n in self.mem:
#             return self.mem[n]

#         res = 0
#         for i in range(1,n+1):

#             left = i-1
#             right = n-i

#             if left not in self.mem:
#                 self.consecutive_combo(left)
#             if right not in self.mem:
#                 self.consecutive_combo(right)


#             res += self.mem[left] * self.mem[right]
#         self.mem[n] = res

#         return res


