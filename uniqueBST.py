# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n: int):
        if not n:
            return []
        memo = {} # 记录

        def generate(s, e):
            if s > e:
                return [None]
            if (s, e) in memo:
                return memo[(s, e)]
            res = []
            for i in range(s, e + 1):
                print(f"** s={s} \t e={e} \t i={i} **")
                print(f"Search: Left: {s}-{i-1}, Right: {i+1}-{e}")
                left = generate(s, i - 1)
                right = generate(i + 1, e)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        print(root.val, root.left.val if root.left else None, root.right.val if root.right else None)
                        res.append(root)
            memo[(s, e)] = res
            return res

        return generate(1, n)


if __name__ == '__main__':
    s = Solution()
    n = 3
    trees = s.generateTrees(n=3)
    print(trees)

