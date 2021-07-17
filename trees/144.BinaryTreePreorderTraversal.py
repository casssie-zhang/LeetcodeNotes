# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # recursively
        # if not root:
        #     return []

        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # iteratively: root, left, right , Stack!
        if not root:
            return []
        res = []
        stack = [root]
        while (stack):
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
