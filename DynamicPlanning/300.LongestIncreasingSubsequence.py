class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp
        ans = 1
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

                ans = max(ans, dp[i])

        return ans
        # greedy