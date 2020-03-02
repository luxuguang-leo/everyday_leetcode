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
        if not head:
            return None
        #@0302, swap 2 nodes
        # dummy node, fast and slow node
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        while head and head.next and head.next.next:
            #narrowdown to slow&fast nodes
            slow = head.next
            fast = head.next.next
            
            #swap them
            head.next = fast
            slow.next = fast.next
            fast.next = slow
            
            #move ahead
            head = slow
        return dummy.next
        
# @lc code=end

