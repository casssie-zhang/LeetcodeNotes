class Solution:
    def numSquares(self, n: int) -> int:

        squarelist = self.generateSquareList(n)
        print(squarelist)
        # for i in range(n):
        #     for j in range(1, i):
        #


    def generateSquareList(self, n):
        squarelist = []
        diff=3
        square=1
        while square <= n:
            squarelist.append(square)
            square += diff
            diff += 2

        return squarelist

s = Solution()
print(s.generateSquareList((16)))
