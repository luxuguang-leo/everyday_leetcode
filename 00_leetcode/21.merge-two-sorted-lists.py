#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #增加新的结点，time O(m+n) space(O max(m, n)+1)
        if not l1:
            return l2
        if not l2:
            return l1
        cur = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                #cur.next = ListNode(l1.val)
                cur.next = l1
                l1 = l1.next
            else:
                #cur.next = ListNode(l2.val)
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        


        