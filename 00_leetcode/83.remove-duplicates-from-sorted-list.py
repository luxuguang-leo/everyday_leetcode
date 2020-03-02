#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
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
        '''
        if not head:
            return head
        dummy = ListNode(float('inf'))
        dummy.next = head
        slow, fast = dummy, head
        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = fast.next
        return dummy.next
        '''
        if not head:
            return None
        dummy = ListNode(float('inf'))
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                dupVal = cur.next.val
                while cur.next.next and cur.next.next.val == dupVal:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
# @lc code=end

