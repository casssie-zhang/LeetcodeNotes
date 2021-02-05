class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        :type s: st
        :type t: str
        :type maxCost: int
        :rtype: int
        """

        # 连续子数组和小于maxCost
        # 滑动窗口
        windowsum = 0
        j = 0
        ans = 0
        record = []

        for i in range(len(s)):
            diff = abs(ord(t[i]) - ord(s[i]))
            record.append(diff)
            # print(i, record)
            windowsum += diff
            while (windowsum > maxCost):
                windowsum -= record[j]
                j += 1

            ans = max(i - j + 1, ans)

        return ans