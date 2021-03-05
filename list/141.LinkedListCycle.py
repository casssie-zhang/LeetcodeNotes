# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #哈希表
        # seen={}
        # while head:
        #     if head in seen:
        #         return True
        #     seen[head]=1
        #     head = head.next

        # return False


        # 快慢指针

        if not head or not head.next:
            return False
        slow = head
        fast = head.next


        slow=head
        fast=head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

