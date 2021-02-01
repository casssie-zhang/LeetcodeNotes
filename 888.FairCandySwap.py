class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = (sum(A) - sum(B)) / 2
        BB = set(B) # set is faster than list
        for i in A:
            if i-diff in BB: # double for loop exceeds time limit
                return [i, i-diff]