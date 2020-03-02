#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
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
        #@0302, same as remove duplicate i
        if not head:
            return None
        dummy = ListNode(float('inf'))
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                dupVal = cur.next.val
                while cur.next and cur.next.val == dupVal:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        
# @lc code=end

