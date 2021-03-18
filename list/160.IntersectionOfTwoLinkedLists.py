class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；同样地，当访问
        # 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。这样就能控制访问 A 和 B
        # 个链表的指针能同时访问到交点。

        # a+c+b = b+c+a
        pos_a, pos_b = headA, headB

        while (pos_a != pos_b):
            # 不要用 if pos_a.next=None
            pos_a = pos_a.next if pos_a else headB
            pos_b = pos_b.next if pos_b else headA

        return pos_a