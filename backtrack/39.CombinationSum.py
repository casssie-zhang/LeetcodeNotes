class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def dfs(path, diff, begin):
            if diff == 0:
                res.append(path)
                # res.add(tuple(sorted(path)))
                return
            if diff < 0:
                return
            for i in range(begin, len(candidates)): # loop all candidates since elements can be used repeatedly
                dfs(path + [candidates[i]], diff - candidates[i], i)

        dfs([], target, 0)


        return list(res)
