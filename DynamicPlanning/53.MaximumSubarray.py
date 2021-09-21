class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]

        res = dp[0]
        for i in range(len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
            res = max(dp[i], res)

        return res