# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        head = tail = ListNode(None)

        while(l1 or l2):
            if not l1:
                tail.next = l2
                break
            if not l2:
                tail.next = l1
                break
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next

        return head.next
