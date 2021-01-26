#1/26 每日一题
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        unique = {} # {a:b} memorize unique dominoes
        for i, (a,b) in enumerate(dominoes):
            sort_pair = tuple(sorted((a,b)))
            if sort_pair in unique:
                unique[sort_pair].append(i)
            else:
                unique[sort_pair] = [i]
        cnt = 0
        for k in unique:
            if len(unique[k])>1:
                cnt += len(unique[k]) * (len(unique[k]) - 1)/2

        return int(cnt)