class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #         if m == 0:
        #             for i in range(n):
        #                 nums1[i] = nums2[i]

        #             return

        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m = m - 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # after this, if m > 0, no need to change
        # if n >0:
        nums1[:n] = nums2[:n]