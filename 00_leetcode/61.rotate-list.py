#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #事实上不需要翻转链表，注意读题目
        #find list size
        '''
        size = 1
        cur = head
        while cur and cur.next:
            cur = cur.next
            size +=1
        k = k % size if size else 0
        if size <= 1 or k == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        ret = cur = slow.next
        while cur and cur.next:
            cur = cur.next
        cur.next = head
        slow.next = None
        return ret
        '''
        #@0302
        #count length of list
        cnt, cur = 0, head
        while cur:
            cnt +=1
            cur = cur.next
        if cnt > 0:
            k = k%cnt
        else:
            k = 0
        if cnt <=1 or k ==0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        fast = slow = dummy
        for _ in range(k):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        newNode = slow.next
        slow.next = None
        fast.next = head
        return newNode
        
        


# @lc code=end

