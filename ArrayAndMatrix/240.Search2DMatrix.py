class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix: return False
        # 横向查找 找到比target小的最大的值
        # 纵向查找 --- 可能会查找不到

        # solution2: 遍历
        # solution3: 折线查找
        row = 0
        col = len(matrix[0]) - 1
        while (row <= len(matrix)-1) and (col >= 0):
            # print(row, col)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1

        return False

s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
s.searchMatrix(matrix, target)