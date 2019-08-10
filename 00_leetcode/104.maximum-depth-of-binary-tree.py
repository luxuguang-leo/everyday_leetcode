#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root:
            return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
        

