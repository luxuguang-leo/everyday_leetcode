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

        def reverseList(head):
            pre = None
            while head:
                nxt = head.next
                head.next = pre
                pre, head = head, nxt
            return pre
        #1.split into two parts
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #2. #2.reverse the second part， now slow.next is the new head
        secondHead = slow.next
        slow.next = None
        secondHead = reverseList(secondHead)
        firstHead = head
        #3.merge them together
        while firstHead and secondHead:
            firstHead.next, firstHead = secondHead, firstHead.next
            secondHead.next, secondHead = firstHead, secondHead.next
        return head

# @lc code=end

