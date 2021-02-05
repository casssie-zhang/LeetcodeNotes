class Solution:
    def searchRange(self, nums, target: int):

        i = 0
        j = len(nums) - 1

        if len(nums) == 1:
            return [-1, -1] if nums[0] != target else [1, 1]

        def find(i, nums, target):
            assert (nums[i] == target)

            l = r = i
            while (r + 1 < len(nums) and nums[r + 1] == target):
                r = r + 1

            while (l - 1 >= 0 and nums[l - 1] == target):
                l = l - 1

            return [l, r]

        while (i < j):
            m = (i + j) // 2

            if nums[m] == target:
                return find(m, nums, target)
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1

        if nums[i] == target:
            return find(i, nums, target)


        return [-1, -1]


s = Solution()
print(s.searchRange([1,4], 4))