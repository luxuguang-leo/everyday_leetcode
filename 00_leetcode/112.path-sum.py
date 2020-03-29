#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #DFS, revrusatively
        '''
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        '''
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, cur_sum = stack.pop()
            if node.left:
                stack.append((node.left, cur_sum+node.left.val))
            if node.right:
                stack.append((node.right, cur_sum+node.right.val))
            if not node.left and not node.right and cur_sum==sum:
                return True
        return False
        '''
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and val == sum:
                return True
            if node.left:
                stack.append((node.left, val + node.left.val))
            if node.right:
                stack.append((node.right, val + node.right.val))
        return False
        
        

