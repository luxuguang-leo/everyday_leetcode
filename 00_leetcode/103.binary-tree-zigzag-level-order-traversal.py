#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
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
        if len(ret) < level+1:
            ret.append([])
        if level%2 == 0:
            ret[level].append(root.val)
        else:
            ret[level].insert(0, root.val)
        self.dfs(root.left, level+1, ret)
        self.dfs(root.right, level+1, ret)
        return ret   

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #@0303, use deque
        #DFS
        '''
        if not root:
            return []
        ret = []
        self.dfs(root, 0, ret)
        return ret
        '''
        #2 deque
        '''
        if not root:
            return []
        q, ret = collections.deque(), []
        q.append(root)
        level_val = 0
        while q:
            level = []
            level_val += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if level_val % 2 == 0:
                        level.insert(0, node.val)
                    else:
                        level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(level)
        return ret
        '''
        #3.deque
        if not root:
            return []
        q, ret = collections.deque(), []
        q.append((root, 1))
        while q:
            l = len(q)
            path = []
            for _ in range(l):
                node, level = q.popleft()
                if level & 0x01:
                    path.append(node.val)
                else:
                    path.insert(0, node.val)
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))
            ret.append(path)
        return ret

