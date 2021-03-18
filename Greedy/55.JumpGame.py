class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_step = 0
        for i in range(len(nums)):
            if i > max_step:
                return False
            max_step = max(i+nums[i], max_step)
        return max_step >= len(nums)-1