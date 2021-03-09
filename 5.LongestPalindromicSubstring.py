class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        self.string = s
        start = 0
        end = 0
        ans = s[0]

        for i in range(len(s)):

            left1, right1 = self.centerExpand(i, i + 1)
            left2, right2 = self.centerExpand(i, i)
            if right2-left2 > end-start:
                start, end = left2, right2
            if right1-left1 > end-start:
                start, end = left1, right1
            print(i, start, end)

        return s[start:end+1]

    def centerExpand(self, i, j):
        # 中心拓展
        while (i >= 0 and j <= len(self.string) - 1):
            if self.string[i] != self.string[j]:
                break
            else:
                j += 1
                i -= 1
        return i + 1, j - 1

s = Solution()
print(s.longestPalindrome("ababb"))