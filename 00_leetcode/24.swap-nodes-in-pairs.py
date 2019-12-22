#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
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
        #两两交换，画图示意
        dummy = ListNode(-1)
        dummy.next = head
        pre, first = dummy, head
        while pre.next and first.next:
            pre.next = first.next
            first.next = first.next.next
            pre.next.next = first
            pre, first = first, first.next
        return dummy.next
        
# @lc code=end

