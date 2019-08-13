#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getdepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getdepth(root.left), self.getdepth(root.right))
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #method 1
        '''
        if not root:
            return True
        leftdepth = self.getdepth(root.left)
        rightdepth = self.getdepth(root.right)
        if abs(leftdepth - rightdepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        #method 2
        

