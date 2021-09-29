# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):

        l1 = ListNode(5)
        l2 = None
        res = self.mergeTwoLists(l1, l2)
        print(res.val)
        # fast and low pointers to find middle node
        # fast = head
        # slow = head
        # while (fast.next and fast.next.next):
        #     fast = fast.next.next
        #     slow = slow.next
        #
        # head2 = slow.next
        # slow.next = None
        #
        # print(head, head2)
        # # sort for the first half and second half
        # head = self.sortList(head)
        # # head2 = self.sortList(head2)
        #
        # return self.mergeTwoLists(head, head2)

    def mergeTwoLists(self, l1, l2):

        res = ListNode(None)
        head = res
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = ListNode(l1.val)
                res = res.next
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next

        if l1:
            res.next = l1
        if l2:
            res.next = l2

        return head.next

if __name__ == '__main__':
    s = Solution()
    s.sortList(None)