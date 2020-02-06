#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        dummy = ListNode(0)
        dummy.next, node = head, dummy
        while node.next  is not None and node.next.next is not None:
            if node.next.val == node.next.next.val:
                pre_value = node.next.val
                while node.next is not None and pre_value == node.next.val:
                    node.next = node.next.next
            else:
                node = node.next
        return dummy.next
        '''

        if not head or not head.next:
            return head
        dummy = ListNode(float('inf'))
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            #如果下一个节点和下下一个节点相等
            #保存下一个节点值，然后往后遍历结点知道出现不相等的值
            if cur.next.val == cur.next.next.val:
                pre = cur.next.val
                while cur.next and cur.next.val == pre:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        

