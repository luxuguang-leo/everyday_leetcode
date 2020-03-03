#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, min_val, max_val):
        if not root:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        return self.dfs(root.right, root.val, max_val) \
            and self.dfs(root.left, min_val, root.val)


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #return self.dfs(root, -float('inf'), float('inf'))

        '''
        #DFS + stack
        stack, pre = [(root, False)], None
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if pre and node.val <= pre.val:
                        return False
                    pre = node
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return True
        '''
        #method 3, DFS+stack
        stack, pre = [], None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if pre and node.val <= pre.val:
                return False
            pre = node
            root = node.right
        return True

