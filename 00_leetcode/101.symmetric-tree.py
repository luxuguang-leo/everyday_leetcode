#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmCore(self, left, right):
        if not left and not right:
            return True
        if left and right:
            if left.val == right.val:
                return self.isSymmCore(left.left, right.right) and self.isSymmCore(left.right, right.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #recursive
        if root:
            return self.isSymmCore(root.left, root.right)
        return True

