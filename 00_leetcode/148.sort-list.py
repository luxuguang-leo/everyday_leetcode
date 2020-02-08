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
    '''
    def merger(self, l, r):
        if not l:
            return r
        if not r:
            return l
        head = ListNode(-1)
        move = head
        while l and r:
            if l.val < r.val:
                move.next = l
                l = l.next
            else:
                move.next = r
                r = r.next
            move = move.next
        move.next = l or r
        return head.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #merge sort
        #1.划分为前后两部分
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(head2)
        return self.merger(l, r)
        '''

    def mergeList(self, first, second):
        if not first:
            return second
        if not second:
            return first
        Node = NewHead = ListNode(-1)
        while first and second:
            if first.val < second.val:
                #Node.next = ListNode(first.val)
                Node.next = first
                first = first.next
            else:
                #Node.next = ListNode(second.val)
                Node.next = second
                second = second.next
            Node = Node.next
        Node.next = first or second
        return NewHead.next
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #merge sort
        if not head or not head.next:
            return head
        #将list切成前后两个部分
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        secondHalf = slow.next
        slow.next = None
        
        #每一部分divide
        firstHalf = self.sortList(head)
        secondHalf = self.sortList(secondHalf)
        #merge 2 sorted list
        return self.mergeList(firstHalf, secondHalf)

        
# @lc code=end

