class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  #
        nums.sort()

        def helper(path, idx):
            # res.add(tuple(path)) # 用集合
            res.append(path)
            for j in range(idx, len(nums)):
                if j != idx and nums[j] == nums[j - 1]:  # TODO:
                    continue
                # print(f"j={j}, nums[j]={nums[j]}", path)
                # dfs
                helper(path + [nums[j]], j + 1)  # avoid using duplicate elements

        helper([], 0)
        return list(res)

        # import itertools
        # for i in range(len(nums)+1):
        #     res += set(itertools.combinations(nums, i))
        # return res
