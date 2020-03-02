#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''
        if not headA or not headB:
            return None
        #find the length of A and B
        M = N = 0
        node = headA
        while node:
            M +=1
            node = node.next
        node = headB
        while node:
            N +=1
            node = node.next
        pA, pB = headA, headB
        if M > N:
            for _ in range(M-N):
                pA = pA.next
        else:
            for _ in range(N-M):
                pB = pB.next
        while pA != pB:
           pA = pA.next
           pB = pB.next
        return pA
        '''
        #another soluction,由于无环，可以在一个链表达到终点的时候指向另外一个list头，这样两个指针的
        #总长度都为两个list长度,如果相等则返回相遇的节点
        if not pA or not pB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next
            pB = pB.next
            if pA == pB:
                return pA
            if not pA:
                pA = headB
            if not pB:
                pB = headA
        return pA
# @lc code=end

