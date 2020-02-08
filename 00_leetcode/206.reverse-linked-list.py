#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #if not head:
            #return None
        #use stack
        '''
        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while stack:
            cur.val = stack.pop()
            cur = cur.next 
        return head
        '''
        #reverse use two pointers, pre and cur, and next
        #       1->       2->       3->      4->       5 
        #pre    cur     next
        #next = cur.next cur.next = pre   pre = cur  cur = next
        '''
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        '''
        #recrusatively 
        #divide LL into 2 parts, first and rest
        #the end of recrusive have 3 conditions:
        #head is None
        #head is last node, head.next is None
        #head is not None
        #link the next of rest to first
        #move first to rest
        '''
        if not head:
            return None
        if not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
        '''
        '''
        stack, cur = [], head
        while cur:
            stack.append(cur)
            cur = cur.next
        cur = newHead = stack.pop()
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return newHead
        '''
        '''
        if not head:
            return head
        pre, cur = None, head
        while cur:
            nxt, cur.next = cur.next, pre
            #cur.next = pre
            pre, cur = cur, nxt
        return pre
        '''
        if not head:
            return head
        pre = None
        while head:
            head.next, pre, head = pre, head, head.next
        return pre
        '''
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead 
        '''
