# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        sentinel = ListNode(0)
        sentinel.next = head
        cursor = head
        prev = sentinel
        while (cursor):
            if not cursor.next:
                break
            # print(cursor)

            prev.next = cursor.next
            nxt = cursor.next.next

            cursor.next.next = cursor
            prev = cursor.next

            cursor.next = nxt
            prev = cursor
            cursor = nxt

        return sentinel.next