#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.helper(left.left, right.right) and self.helper(left.right, right.left)
        return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #@0302,一个方式是寻找有限为正确的解，然后别的直接判为false
        '''
        if root:
            return self.helper(root.left, root.right)
        return True
        '''
        #BFS,use stack way
        if not root:
            return True
        if not root.left and not root.right:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append((left.right, right.left))
            stack.append((left.left, right.right))
        return True


        
# @lc code=end

