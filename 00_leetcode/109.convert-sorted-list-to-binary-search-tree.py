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
        #破题，linked list只能单向访问，BST是一个二叉树，一般需要迭代生成，目标找到中间值，然后左右子树迭代
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = head, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        newNode = slow.next
        root = TreeNode(newNode.val)
        slow.next = None
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(newNode.next)
        return root


