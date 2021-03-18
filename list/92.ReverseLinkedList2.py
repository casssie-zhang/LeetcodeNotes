# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        sentinel = ListNode(0)
        sentinel.next = head
        # 因为头节点有可能发生变化，使用虚拟头节点可以避免复杂的分类讨论
        begin, end, reverse_head, reverse_end = sentinel, None, None, None

        for i in range(left - 1):
            begin = begin.next

        tail = begin.next  # 反转后的链表的结尾节点
        cur = begin.next  # 当前节点

        for i in range(left - 1, right):
            nxt = cur.next
            cur.next = reverse_head
            reverse_head = cur
            cur = nxt

        begin.next = reverse_head
        tail.next = cur

        # reversed_end.next = end

        return sentinel.next