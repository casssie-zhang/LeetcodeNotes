class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        end = intervals[0][1]
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                continue
            else:
                cnt += 1
                end = intervals[i][1]
                print(intervals[i])

        return len(intervals)-cnt





if __name__ == '__main__':
    s = Solution()
    interval = [[1,2], [2,3], [1,6], [1,4], [5,7]]
    print(s.eraseOverlapIntervals(interval))
    interval = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    print(s.eraseOverlapIntervals(interval))
