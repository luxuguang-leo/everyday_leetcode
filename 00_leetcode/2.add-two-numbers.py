#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
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
        '''
        dummy = cur = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry /= 10
        return dummy.next
        '''
        #no need to allocate extra space
        carry = l1.val + l2.val
        l1.val = carry %10
        carry = carry/10
        ret = l1
        while l1.next and l2.next:
            carry += (l1.next.val + l2.next.val)
            l1.next.val = carry%10
            carry /= 10
            l1 = l1.next
            l2 = l2.next
        if l2.next:
            l1.next = l2.next
        while l1.next and carry:
            carry += l1.next.val
            l1.next.val = carry%10
            carry /= 10
            l1 = l1.next
        if carry:
            l1.next = ListNode(carry)
        return ret
        
# @lc code=end

