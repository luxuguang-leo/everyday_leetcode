#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS+recrusative
        '''
        if not root:
            return 0
        if root:
            return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''
        #DFS+stack, 32ms
        '''
        if not root:
            return 0
        stack = [(root, 1)]
        ret = 0
        while stack:
            root, level = stack.pop()
            ret = max(ret, level)
            if root.left:
                stack.append((root.left, level+1))
            if root.right:
                stack.append((root.right, level+1))
        return ret
        '''
        #BFS+queue, 40ms
        '''
        if not root:
            return 0
        ret = 0
        q = [(root, 1)]
        while q:
            node, level = q.pop(0)
            ret = max(ret, level)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return ret
        '''
        #BFS+queue, optimize， 28ms
        '''
        if not root:
            return 0
        q = [(root, 1)]
        while q:
            node, level = q.pop(0)
            #最后一个结点的判断
            if not node.left and not node.right and not q:
                return level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            
        #return ret
        '''
        #@0303, 20ms
        if not root:
            return 0
        stack = [(root, 1)]
        ret = 0
        while stack:
            node, level = stack.pop()
            if level > ret:
                ret = level
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return ret
        
        

