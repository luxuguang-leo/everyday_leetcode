#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return self.countNodes(root.left) + self.countNodes(root.right) +1
        if not root.left and root.right:
            return self.countNodes(root.right) +1
        if not root.right and root.left:
            return self.countNodes(root.left) +1
        return 1

        

