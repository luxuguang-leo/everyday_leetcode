#
# @lc app=leetcode id=445 lang=python
#
# [445] Add Two Numbers II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    '''

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverseList(head):
            pre = None
            while head:
                nxt = head.next
                head.next = pre
                pre, head = head, nxt
            return pre
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry = carry//10
            cur = cur.next
        return reverseList(dummy.next)

        

