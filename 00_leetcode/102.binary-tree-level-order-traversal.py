#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, level, ret):
        if not root:
            return
        if len(ret) < level +1:
            ret.append([])
        ret[level].append(root.val)
        self.dfs(root.left, level + 1, ret)
        self.dfs(root.right, level + 1, ret)
        return ret

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #method 1
        '''
        if not root:
            return []
        ret = []
        if root:
            self.dfs(root, 0, ret)
        return ret
        '''
        #method 2
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        ret = []
        while q:
            level = []
            for x in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(level)
        return ret
        

