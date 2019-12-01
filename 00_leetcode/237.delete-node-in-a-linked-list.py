#
# @lc app=leetcode id=237 lang=python
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #将node后一个结点复制到当前节点，然后直接将当前节点指向next.next
        node.val, node.next = node.next.val,node.next.next

        
# @lc code=end

