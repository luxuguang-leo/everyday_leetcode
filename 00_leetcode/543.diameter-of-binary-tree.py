#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.ret = 0
        def getDepth(root):
            if not root:
                return 0
            L = getDepth(root.left)
            R = getDepth(root.right)
            self.ret = max(self.ret, 1 + L + R)
            return 1 + max(L, R)
        getDepth(root)
        return self.ret - 1
# @lc code=end

