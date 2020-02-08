#
# @lc app=leetcode id=328 lang=python
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #奇，偶交替使用两个指针
        if not head:
            return head
        odd, even, evenHead = head, head.next, head.next
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
        #直观做法
        '''
        if not head or not head.next:
            return head
        odd = dummy1 = ListNode(-1)
        even = dummy2 = ListNode(-1)
        cnt = 0
        while head:
            cnt +=1
            if cnt % 2 ==1:#odd
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
        odd.next = dummy2.next
        even.next = None
        return dummy1.next
        '''

        
# @lc code=end

