#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #list operation, simple but need carful implementation 
        #需要新建一些列表能否直接在原有列表增加呢？
        '''
        dummp = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry %10)
            cur = cur.next
            carry = carry/10
        return dummp.next
        '''
        tmp = (l1.val + l2.val)/10
        l1.val = (l1.val + l2.val)%10
        ret = l1
        while l1.next and l2.next:
            tmp += l1.next.val + l2.next.val
            l1.next.val, tmp = tmp%10, tmp/10
            l1 = l1.next
            l2 = l2.next
        if l2.next:
            l1.next = l2.next
        while l1.next and tmp:
            tmp += l1.next.val
            l1.next.val, tmp = tmp%10, tmp/10
            l1 = l1.next
        if tmp:
            l1.next = ListNode(tmp)
        return ret

            


