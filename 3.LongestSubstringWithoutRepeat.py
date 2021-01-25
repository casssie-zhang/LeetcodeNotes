class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        showup = {}
        dp = [0 for i in s]
        ans = 0 # 记录答案
        for i in range(len(s)):
            if s[i] in showup:
                dp[i] = min(dp[i-1]+1, i - showup[s[i]])
                showup[s[i]] = i # 记录出现的index

            else:
                showup[s[i]] = i
                dp[i] = dp[i-1] + 1

            ans = max(dp[i], ans)

        return ans


        # 滑动窗口
    # def slidewindow(self, s):
    #     set = ()
    #     for i in range(len(s)):
    #         c = s[i]
    #         if c in set:
    #             loc = 0
    #             j = 0
    #             while(j < i):
    #                 if s[j] == c:
    #                     loc = j
    #                  j += 1
    #         else:
    #             set.add(c)
    #
    #         ans = max(ans, i - loc)
    #
    #     return ans


inputs = ["abcabcbb"]
s = Solution()
s.lengthOfLongestSubstring(inputs)