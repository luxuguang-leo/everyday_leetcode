#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = nextHead = ListNode(-1)
        l = r  =  dummy.next = head
        #类似于滑动串口，先让右边界走K步，然后在[l, r]范围内反转链表
        #然后将左边界扩展到r,重复上一步，知道走的步数不是k证明到了链表尾部
        while True:
            cnt = 0
            while r and cnt < k:
                cnt +=1
                r = r.next
            if cnt == k:
                pre, cur = r, l
                for _ in range(k):
                    nxt = cur.next
                    cur.next = pre
                    pre, cur = cur, nxt
                #这个nextHead应该是前面一组的尾结点，这时候需要
                #1.将前一组的接到新的头pre
                #2.前一组的尾更新，之前的l现在变成了当前组的尾巴，所以应该更新为它
                #3.左边界l应该更新为r
                nextHead.next = pre
                nextHead = l
                l = r
            else:
                return dummy.next
        

