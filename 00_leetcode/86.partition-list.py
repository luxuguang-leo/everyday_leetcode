#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#
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
        dummy1, dummy2 = ListNode(0), ListNode(0)
        leftTail, rightTail = dummy1, dummy2
        while head:
            if head.val < x:
                leftTail.next = head
                leftTail = leftTail.next
            else:
                rightTail.next = head
                rightTail = rightTail.next
            head = head.next
        rightTail.next = None
        leftTail.next = dummy2.next
        return dummy1.next


