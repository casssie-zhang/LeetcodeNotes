"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, node: 'Node') -> 'Node':

        # TODO: BFS
        """
        node is the pointer in the parent level,
        tail is the tail pointer in the child level.

        parent level can be seen as a linked list
        """

        root = node
        tail = dummy = Node(0)

        while node:

            # tail.next = node.left # at this time, dummy.next = node.left
            # if tail.next:
            #     tail = tail.next
            # tail.next = node.right
            # if tail.next:
            #     tail = tail.next

            for c in (node.left, node.right):
                tail.next = c
                if tail.next:
                    tail = tail.next  # 如果node.left是None，则下一次loop会更新

            if node.next:
                node = node.next
            else:
                node = dummy.next
                tail = dummy
        return root

    # TODO: below is the solution of Level Order Traversal
#         if not root:
#             return

#         root.next = None
#         self.level_connect([root])

#         return root


#     def level_connect(self, last_level):
#         if not last_level:
#             return
#         this_level = []

#         for root in last_level:
#             if root.left:
#                 this_level.append(root.left)
#             if root.right:
#                 this_level.append(root.right)

#         # print([x.val for x in this_level])

#         this_level.append(None)
#         for i in range(len(this_level)-1):
#             this_level[i].next = this_level[i+1]

#         this_level.pop()

#         self.level_connect(this_level)

