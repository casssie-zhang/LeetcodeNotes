# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cursor = head
        while(cursor):
            if not cursor.next:
                break
            if cursor.val == cursor.next.val:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next

        return head