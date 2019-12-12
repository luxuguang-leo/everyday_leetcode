#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rootMax(self, root):
        if not root:
            return float('-inf')
        l = max(0, self.rootMax(root.left))
        r = max(0, self.rootMax(root.right))
        self.ans = max(self.ans, l + r + root.val)
        return root.val + max(l, r)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS,考虑多种情况，对每一个节点左右求解取val+max(left, right, 0)
        self.ans = float('-inf')
        self.rootMax(root)
        return self.ans
        
        

