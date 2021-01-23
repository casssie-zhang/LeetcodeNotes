# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.cnt = 0
        if not root:
            return 0

        def dfs(root, sumlist):
            if not root:
                return


            sumlist = [root.val + num for num in sumlist] + [root.val]
            for s in sumlist:
                if s == sum:
                    self.cnt += 1

            dfs(root.left, sumlist)
            dfs(root.right, sumlist)



        dfs(root, [])

        return self.cnt