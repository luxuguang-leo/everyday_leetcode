#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
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
        if len(ret) < level+1:
            ret.append([])
        ret[level].append(root.val)
        self.dfs(root.left, level+1, ret)
        self.dfs(root.right, level +1, ret)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #dfs
        ret = []
        self.dfs(root, 0, ret)
        return ret
        #deque
        '''
        if not root:
            return []
        q, ret= collections.deque(), []
        q.append(root)
        while q:
            path = []
            for _ in range(len(q)):
                node = q.popleft()
                path.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(path)
            #node = q.pop(0)
        return ret
        '''
        #queue
        '''
        if not root:
            return []
        q, ret = [root], []
        while q:
            path = []
            l = len(q)
            while l > 0:
                node = q.pop(0)
                if node:
                    path.append(node.val)
                if node.left:    
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l -=1
            ret.append(path)
        return ret
        '''

        
# @lc code=end

