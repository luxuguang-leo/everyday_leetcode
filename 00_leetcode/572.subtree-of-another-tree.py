#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
# @lc code=end

