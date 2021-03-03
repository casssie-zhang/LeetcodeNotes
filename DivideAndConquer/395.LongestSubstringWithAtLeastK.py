class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # # divide and conquer
        if len(s) < k:
            return 0  # return the length!

        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)