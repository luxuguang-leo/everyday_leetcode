#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #DFS
        '''
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        '''
        #BFS
        q = collections.deque([root])
        #q.append(root)
        while q:
            node = q.pop()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root


        
