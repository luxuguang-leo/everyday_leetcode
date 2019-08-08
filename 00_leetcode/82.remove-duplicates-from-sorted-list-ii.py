#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next, node = head, dummy
        while node.next  is not None and node.next.next is not None:
            if node.next.val == node.next.next.val:
                pre_value = node.next.val
                while node.next is not None and pre_value == node.next.val:
                    node.next = node.next.next
            else:
                node = node.next
        return dummy.next

