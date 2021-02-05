class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -10000
        if len(nums) <= 4:
            return sum(nums) / len(nums)
        start = nums[0]
        prevsum = sum(nums[:k])
        maxsum = sum(nums[:k])

        for i in range(k, len(nums)):
            # print(i, start)
            # if nums[i] > start:
            maxsum = max(maxsum, prevsum-start+nums[i])
            prevsum = prevsum-start+nums[i]
            start = nums[i-k+1]

        return maxsum/k