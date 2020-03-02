#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        '''
        if not head:
            return None
        dummyHead1, dummyHead2 = ListNode(-1), ListNode(-1)
        head1, head2 = dummyHead1, dummyHead2
        while head:
            if head.val < x:
                head1.next = head
                head1 = head1.next
            else:
                head2.next = head
                head2 = head2.next
            head = head.next
        head2.next = None
        head1.next = dummyHead2.next
        return dummyHead1.next
        '''
        if not head:
            return head
        small, large = ListNode(0), ListNode(0)
        l, r, cur = small, large, head
        while cur:
            if cur.val < x:
                small.next = cur
                small = small.next
            else:
                large.next = cur
                large = large.next
            cur = cur.next
        small.next = r.next
        large.next = None
        return l.next
# @lc code=end

