class Solution:
    def kthSmallest(self, matrix, k) -> int:
        # # Solution1: python brute force
        # flatten = []
        # for row in matrix:
        #     flatten += row

        # return sorted(flatten)[k-1]
        def check(mid):
            row, col = len(matrix) - 1, 0
            cnt = 0  # number of elements that smaller than k
            while row >= 0 and col <= len(matrix[0]) - 1:
                if matrix[row][col] > mid:
                    #             # cnt += col+1
                    row -= 1
                else:
                    cnt += row + 1
                    col += 1

            return cnt >= k

        # 沿着对角线二分查找
        l, r = matrix[0][0], matrix[-1][-1]  # min and max
        while (l < r):
            m = (l + r) // 2
            if check(m):  # cnt>=k 可能 m就是答案
                r = m
            else:
                l = m + 1
        return l


s = Solution()
arr = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(s.kthSmallest(arr, k))