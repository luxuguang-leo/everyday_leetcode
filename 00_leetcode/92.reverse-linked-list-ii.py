#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        #@0302, practise
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        #first move to the node before moving
        for _ in range(m-1):
            p = p.next
        #use reversing method, Node: reverse, cur, next
        #we move 1 more steps, the cur node will be the out of range
        cur = p.next 
        reverse = None
        for _ in range(n-m+1):
            tmp = cur.next
            cur.next = reverse
            reverse = cur
            cur = tmp
        #after that need to fix the final state
        # 1 -> 2 <—— 3 <—— 4 <—— 5 -> None
        #      |        reverse cur
        #      Y
        #      None
        p.next.next = cur #link 2->5
        p.next = reverse   #link 1->4
        #finaly, 1——>4 ——> 3 ——>2 ——>5 ->None
        return dummy.next
        
        

