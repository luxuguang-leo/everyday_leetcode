#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next:#while跳出循环没有满足相等条件
            return None
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast

    