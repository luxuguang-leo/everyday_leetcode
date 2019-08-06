#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while pre.next and cur.next:
            pre.next = cur.next
            cur.next = pre.next.next
            pre.next.next = cur
            pre, cur = cur, cur.next
        return dummy.next

        

