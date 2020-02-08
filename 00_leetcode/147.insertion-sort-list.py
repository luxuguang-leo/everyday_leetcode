#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                #swap if next node is large
                #@02.08 update, not swap, insert the smaller node in the first sorted list
                #1.fetch next node
                tmp = cur.next
                #2.delete next node
                cur.next = cur.next.next
                #3.travel from head to find the node large than tmp node
                tHead = dummy
                while tHead.next and tHead.next.val < tmp.val:
                    tHead = tHead.next
                #insert after node
                tmp.next = tHead.next
                tHead.next = tmp
        return dummy.next
        
        
# @lc code=end

