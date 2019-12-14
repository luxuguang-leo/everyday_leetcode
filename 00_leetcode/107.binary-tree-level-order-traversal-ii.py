#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
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
            return root
        if len(ret) < level + 1:
            ret.insert(0, [])
        ret[-level-1].append(root.val)
        self.dfs(root.left, level+1, ret)
        self.dfs(root.right, level+1, ret)
        return ret
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #1 recrusively
        '''
        if not root:
            return []
        ret = []
        self.dfs(root, 0, ret)
        return ret

        '''

        #2 interavtive
        '''
        if not root:
            return []
        ret = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for X in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.insert(0, level)
        return ret
        '''
        #BFS + queue
        if not root:
            return []
        q, ret = [root], []
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.insert(0, level)
        return ret


