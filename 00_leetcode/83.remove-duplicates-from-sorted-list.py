#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
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
        '''
        if not head or not head.next:
            return head
        p = head
        while p and p.next:
            next = p.next
            if p.val == next.val:
                p.next = next.next
                continue
            p = p.next
        return head
        '''
        #elegant soluction
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
        
        

