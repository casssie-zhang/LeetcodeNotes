class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # special case
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        i = 0
        j = len(nums) - 1
        while (i <= j):
            mid = (i+j) // 2
            if nums[mid] > target and nums[mid-1] < target:
                return mid
            if nums[mid] > target:
                j = mid-1
            else:  # <=
                i = mid+1

        return i+1

s = Solution()
ans = s.searchInsert([1,3,5,9], 2)
assert (ans == 1)

ans = s.searchInsert([1,3,5,9], 8)
assert (ans == 3)

ans = s.searchInsert([1,3,5,9], 4)
assert (ans == 2)