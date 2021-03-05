class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        # envelopes_w = sorted(envelopes)
        # ** 按长度排序，之后解决300.最长递增子序列问题
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        # ans = 1

        dp = [1] * len(envelopes)
        # print(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    # print(dp)
                    # ans = max(ans, dp[i])
        return max(dp)


s = Solution()
# print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(s.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))
