#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        if not root:
            return 0
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        return 1+ min(self.minDepth(root.left), self.minDepth(root.right))
        '''
        #BFS, use deque
        '''
        if not root:
            return 0
        q = collections.deque()
        q.append([root, 1])
        while q:
            node, level = q.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    q.append((node.left, level+1))
                    q.append((node.right, level+1))
        '''
        if not root:
            return 0
        q  = [(root, 1)]
        while q:
            node, level = q.pop(0)
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    q.append((node.left, level+1))
                    q.append((node.right, level+1))

