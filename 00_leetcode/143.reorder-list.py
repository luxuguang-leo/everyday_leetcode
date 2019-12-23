#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
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

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #1.split into two parts
        if not head or not head.next or not head.next.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #2.reverse the second part， now slow.next is the new head
        pre = None
        head2 = slow.next
        slow.next = None
        while head2:
            nxt = head2.next
            head2.next = pre
            pre = head2
            head2 = nxt
        #3.mix the half 2 parts together
        first, second = head, pre
        while second:
            first.next, first = second, first.next
            #print(first, second)
            second.next, second = first, second.next
        return head


            
        
# @lc code=end

