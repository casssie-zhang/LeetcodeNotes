class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        i, j = 0, len(s) - 1
        s = list(s)
        while (i < j):
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1

            elif s[i] in vowels and s[j] in vowels:
                s[j], s[i] = s[i], s[j]
                i += 1
                j -= 1
        return ''.join(s)