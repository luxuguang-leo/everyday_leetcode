#
# @lc app=leetcode id=965 lang=python
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        if not root:
            return True
        val = root.val
        s = [root]
        while s:
            node = s.pop()
            if node.val != val:
                return False
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return True
        '''
        if not root:
            return True
        if root.left:
            if root.left.val != root.val:
                return False
        if root.right:
            if root.right.val != root.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        
# @lc code=end

