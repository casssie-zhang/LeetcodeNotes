class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        #二分查找
        # l = 0
        # h = len(letters)-1
        #
        # while (l <= h):
        #     m = (l + h) // 2
        #     if letters[m] > target:
        #         h = m-1
        #     if letters[m] <= target:
        #         l = m+1
        #
        #
        #
        # return letters[l if l < len(letters) else 0]

        for i, l in enumerate(letters):
            if l > target:
                return letters[i if i < len(letters) else 0]

        return letters[0]


inputs = ["c", "f", "j", "k", "z"]
s = Solution()

print("===")

target = "k"
print(s.nextGreatestLetter(inputs, target))

print("===")

target="a"
print(s.nextGreatestLetter(inputs, target))

print("===")

target="d"
print(s.nextGreatestLetter(inputs, target))
#
print("===")

target="z"
print(s.nextGreatestLetter(inputs, target))