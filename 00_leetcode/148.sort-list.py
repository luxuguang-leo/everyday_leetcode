#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeCore(self, l, r):
        cur = dummy = ListNode(-1)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #@0303
        #merge and sort
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        #divide into two parts
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slow.next should be head of second part
        secondHead = slow.next
        slow.next = None
        #divide left and right part
        left = self.sortList(head)
        right = self.sortList(secondHead)
        #merge the sorted list
        return self.mergeCore(left, right)



