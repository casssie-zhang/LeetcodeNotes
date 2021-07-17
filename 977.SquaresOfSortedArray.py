class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([i*i for i in nums])
        i, j = 0, len(nums) - 1
        res = [0] * len(nums)
        pos = len(nums) - 1

        while (i <= j):
            if abs(nums[j]) >= abs(nums[i]):
                res[pos] = nums[j] * nums[j]
                j = j - 1

            else:
                res[pos] = nums[i] * nums[i]

                i = i + 1
            pos = pos - 1
        return res