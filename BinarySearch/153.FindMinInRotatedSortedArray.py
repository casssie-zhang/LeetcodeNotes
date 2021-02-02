class Solution:
    def findMin(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        i = 0
        j = len(nums)-1

        while(i<j):
            m = (i+j) // 2
            # print(i, j, m)
            # if nums[m] <= nums[m-1]:
            #     return nums[m]

            if nums[m] > nums[j]:
                i = m + 1
            elif nums[m] < nums[i]:
                j = m # m still could be answer?
            else: # 单调
                return nums[i]
        return nums[i]

        # left, right = 0, len(nums) - 1  # 左闭右闭区间，如果用右开区间则不方便判断右值
        # while left < right:  # 循环不变式，如果left == right，则循环结束
        #     mid = (left + right) >> 1  # 地板除，mid更靠近left
        #     if nums[mid] > nums[right]:  # 中值 > 右值，最小值在右半边，收缩左边界
        #         left = mid + 1  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
        #     elif nums[mid] < nums[right]:  # 明确中值 < 右值，最小值在左半边，收缩右边界
        #         right = mid  # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
        # return nums[left]  # 循环结束，left == right，最小值输出nums[left]或nums[right]均可
        #
        #
        # 作者：armeria - program
        # 链接：https: // leetcode - cn.com / problems / find - minimum - in -rotated - sorted - array / solution / er - fen - cha - zhao - wei - shi - yao - zuo - you - bu - dui - cheng - z /
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


s = Solution()
print(s.findMin([2,1]))
print(s.findMin([4,5,6,7,0,1,2]))
#
print(s.findMin([3,4,5,1,2]))
#
print(s.findMin([1,2,3,4,5,6,7]))
print(s.findMin([3,1,2]))