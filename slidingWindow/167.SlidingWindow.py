class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        look = {}
        for i in range(len(numbers)):
            if numbers[i] in look:
                return [look[numbers[i]]+1, i+1]
            else:
                look[target-numbers[i]] = i