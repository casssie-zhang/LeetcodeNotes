class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # # Solution1: built-in package
        # import itertools
        # res = [[]]
        # for x in range(1, len(nums)+1):
        #     for y in itertools.combinations(nums, x) :
        #         res.append(y)
        # return res

        # Solution2:iteratively
        # res = [[]]
        # for i in nums:
        #     res = res + [e+[i] for e in res]

        # return res

        # Solution 3 回溯

        res = []

        def helper(path, j):
            res.append(path)
            for i in range(j, len(nums)):
                helper(path + [nums[i]], j=i + 1)

        helper([], 0)  # init
        return res