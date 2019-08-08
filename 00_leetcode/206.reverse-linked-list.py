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
        #1>>use stack
        '''
        p = head
        list_new = []
        while p:
            list_new.insert(0, p.val)
            p = p.next
        p = head
        for data in list_new:
            p.val = data
            p = p.next
        return head
        '''
        #2, insert for the head of linklist
        #different with previous thought
        #       1 ->    2 ->    3 ->     4 ->    NULL
        # pre   cur ->  next
        # NULL<- 1      2->     3->      4->     NULL
        # NULL<- 1  <-  2       3->      4->     NULL
        '''
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
        '''
        #2 elegant soluction
        '''
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next, pre, cur = pre, cur, next
        return pre
        '''
        #recrusive
        #divide LL into 2 parts, first and rest
        #the end of recrusive have 3 conditions:
        #head is None
        #head is last node, head.next is None
        #head is not None
        #link the next of rest to first
        #move first to rest
        if head is None:
            return head
        if head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
