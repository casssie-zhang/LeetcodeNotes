class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # TODO: 滑动窗口，双指针
        left=0
        right=-1
        num = [0] * 26
        max_cnt = 0
        while(right<len(s)-1):
            right += 1 # 右指针向右移动
            # print("@right:", right, s[right])
            # 记录出现次数
            num[ord(s[right])-ord("A")] += 1
            # print(num[:3])
            max_cnt = max(num[ord(s[right])-ord("A")], max_cnt)
            if right-left+1-max_cnt>k:
                # print("***left pointer moving***")
                num[ord(s[left])-ord("A")] -= 1
                left += 1
        return right-left+1

s = Solution()
k=2
inputs = "AABCABBB"
print(s.characterReplacement(inputs, 2))

inputs = "ABAB"
print(s.characterReplacement(inputs, 2))