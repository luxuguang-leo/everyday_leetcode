#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs2(self, root, level, ret):
        if not root:
            return ret
        if len(ret) == level:
            ret.append(root.val)
        self.dfs2(root.right, level+1,ret)
        self.dfs2(root.left, level+1,ret)
        '''
        def dfs(self, root, level, ret):
        if not root:
            return 
        if len(ret) < level +1:
            ret.append([])
        ret[level].append(root.val)
        self.dfs(root.right, level+1, ret)
        self.dfs(root.left, level+1, ret)
        '''
        

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #DFS,取自身，可以看做之前层次遍历的延伸，去层次遍历的最后一个值即可
        '''
        if not root:
            return []
        ret = []
        self.dfs(root, 0, ret)
        return [x[0] for x in ret]
        '''
        #DFS,rework
        '''
        if not root:
            return []
        ret = []
        self.dfs2(root, 0, ret)
        return ret
        '''
        #BFS
        '''
        if not root:
            return []
        q, ret = collections.deque(), []
        q.append(root)
        while q:
            path = []
            for i in range(len(q)):
                node = q.popleft()
                path.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            ret.append(path)
        return [x[0] for x in ret]
        '''
        q, ret = collections.deque(),[]
        if not root:
            return ret
        q.append((root, 0))
        while q:
            for _ in range(len(q)):
                node, level = q.popleft()
                if len(ret) == level:
                    ret.append(node.val)
                if node.right:
                    q.append((node.right, level+1))
                if node.left:
                    q.append((node.left, level+1))
        return ret
# @lc code=end

