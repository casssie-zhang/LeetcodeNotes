# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1: return l2
        if not l2: return l1
        head = tail = ListNode(None)
        add = 0

        while (l1 or l2 or add): #TODO: trick! if add == 0 --> False
            # 如果为空 用零代替
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + add

            tail.next = ListNode(val if val <= 9 else val % 10)

            add = val // 10  # 进位值

            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next