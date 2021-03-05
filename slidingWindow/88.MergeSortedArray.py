class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Solution: merge + sort
        # nums1[:] = sorted(nums1[:m] + nums2)

        # Solution2:
        i = m - 1
        j = n - 1
        while (j >= 0 and i >= 0):
            if nums1[i] < nums2[j]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]

