class Solution:
    def maxProduct(self, nums: list) -> int:
        # 最大值*正数=最大值
        # 最大值*负数=最小值
        # 最小值*正数=最小值
        # 最小值*负数=最大值
        # solution1 : 动态规划
        # TODO: 怎么节省空间到O(n)

        if not nums:
            return 0

        dp = [[0, 0] for i in nums]
        dp[0][0], dp[0][1] = nums[0], nums[0]

        res = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if num >= 0:
                # fst = num * dp[i-1]
                dp[i][0] = min(num, num * dp[i-1][0]) # min
                dp[i][1] = max(num, num * dp[i-1][1]) # max

            else:
                dp[i][0] = min(num, num * dp[i-1][1])
                dp[i][1] = max(num, num * dp[i-1][0])

            print(dp)

            res = max(res, dp[i][1])

        return res



if __name__ == '__main__':
    s = Solution()
    inputs = [2,3,-2,4]
    print(s.maxProduct(inputs))