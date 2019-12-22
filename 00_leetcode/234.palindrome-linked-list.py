#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #really easy?find the half point and reverse the other part, compare if there are the same
        '''
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        newPart = self.reverseList(slow)
        slow = head
        while newPart and slow:
            if newPart.val != slow.val:
                return False
            slow = slow.next
            newPart = newPart.next
        return True
        '''
        #use stack
        if not head or not head.next:
            return True
        stack = []
        fast = slow = head
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True

        
# @lc code=end

