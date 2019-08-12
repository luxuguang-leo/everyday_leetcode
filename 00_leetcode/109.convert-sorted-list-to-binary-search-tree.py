#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        ##linked list and BST
        #first use 2 pointers to find the middle val
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        root = TreeNode(slow.next.val)
        tmp = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(tmp)
        return root

