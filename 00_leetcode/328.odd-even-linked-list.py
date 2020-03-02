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
        odd = dummy1 = ListNode(-1)
        even = dummy2 = ListNode(-1)
        cur, cnt = head, 0
        while cur:
            cnt +=1
            if cnt & 0x01:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
        odd.next = dummy2.next
        even.next = None
        return dummy1.next
        
# @lc code=end

