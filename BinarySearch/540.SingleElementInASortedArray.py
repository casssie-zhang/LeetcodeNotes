class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while (i < j):
            m = (i + j) // 2
            # print(f"i={i}, j={j}, m={m}")
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            else:
                if m % 2 == 0:  # m 是偶数
                    if nums[m] == nums[m - 1]:  # second
                        j = m - 1
                    elif nums[m] == nums[m + 1]:
                        i = m + 1
                else: # m is odd
                    if nums[m] == nums[m - 1]: # second
                        i = m + 1
                    elif nums[m] == nums[m+1]:
                        j = m - 1
        return nums[i]

s = Solution()
inputs=[1,2,2,3,3,4,4,8,8]
print(s.singleNonDuplicate(inputs))

inputs=[1,1,2,3,3,4,4,8,8]
print(s.singleNonDuplicate(inputs))

inputs=[1,1,2,2, 3,3,4,4,8]
print(s.singleNonDuplicate(inputs))