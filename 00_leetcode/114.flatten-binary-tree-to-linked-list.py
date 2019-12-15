#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        while root:
            if root.left:
                self.flatten(root.left)
                newleft = root.left#already flatten left part
                while newleft.right:
                    newleft = newleft.right
                newleft.right = root.right
                root.left, root.right = None, root.left
            root = root.right
        
        
# @lc code=end

