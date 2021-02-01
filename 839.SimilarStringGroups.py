class Solution:
    def numSimilarGroups(self, strs) -> int:

        n = len(strs)
        f = list(range(n))

        def find(x: int) -> int:
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def check(a: str, b: str) -> bool:
            pos = 0
            for i, j in zip(a, b):
                if i != j:
                    pos += 1

            if pos > 2: #strs are anagram of any other strs. 1 can't exist. 0 - indentical, 2 - similar
                return False

            return True

        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if check(strs[i], strs[j]):
                    f[fi] = fj  # fi的父节点设为j

        ret = sum(1 for i in range(n) if f[i] == i)
        return ret



# # two words are not similar directly but they can be connected by another word
abc = ["tars","rats","arts","star"]
s = Solution()
print(s.numSimilarGroups(abc))