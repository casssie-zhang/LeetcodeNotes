# class Solution:
#     def search(self, nums, target):
#         first, last = 0, len(nums)
#         while(first != last):
#             mid = first + (last - first) // 2
#             if nums[mid] == target:
#                 return mid
#
#             if nums[first] <= nums[mid]:
#                 if nums[first] <= target and target < nums[mid]:
#                     last = mid
#                 else:
#                     first = mid + 1
#             else:
#                 if nums[mid] < target and target <= nums[last-1]:
#                     first = mid
#                 else:
#                     last = mid + 1
#
#         return -1

class Solution:
    def search(self, nums, target):
        first, last = 0, len(nums)-1
        while(first <= last):
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return mid

            if nums[first] <= nums[mid]:
                if nums[first] <= target and target < nums[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
            else:
                if nums[mid] < target and target <= nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1

        return -1

test1 = [4,5,6,7,8,0,1,2,3]
s = Solution()
# print(s.search(test1, 0))


assert s.search(test1, 0) == 5
assert s.search(test1, 3) == 8
assert s.search(test1, 4) == 0
assert s.search(test1, 8) == 4

test2 = [0]
assert s.search(test2, 0) == 0
assert s.search(test2, 1) == -1

# print(s.search(test1, 3))
# print(s.search(test1, 1))
# print(s.search(test1, 4))