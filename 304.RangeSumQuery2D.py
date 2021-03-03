class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix if matrix else None
        # 累加矩阵
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lt = self.matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                l = self.matrix[i][j - 1] if j > 0 else 0
                t = self.matrix[i - 1][j] if i > 0 else 0
                self.matrix[i][j] = self.matrix[i][j] + t + l - lt

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # res = 0
        # for i in range(row1, row2+1):
        #     # print(self.matrix[i][col1:col2+1])
        #     res += sum(self.matrix[i][col1:col2+1])
        # return res

        return self.matrix[row2][col2] - (self.matrix[row2][col1 - 1] if col1 > 0 else 0) - (
            self.matrix[row1 - 1][col2] if row1 > 0 else 0) + (
                   self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)