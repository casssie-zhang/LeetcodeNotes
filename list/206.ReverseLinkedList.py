# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # iteratively insert from head
        # reversehead=None
        # while head!=None:
        #     headnext=head.next
        #     head.next=reversehead
        #     reversehead=head
        #     head=headnext

        # return reversehead

        # recursively
        # if not head or not head.next: return head
        # res = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return res