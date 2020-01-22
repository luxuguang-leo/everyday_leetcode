#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path_sum, ret):
        if not root:
            return 
        if not root.left and not root.right:
            ret.append(path_sum)
        if root.left:
            self.dfs(root.left, path_sum*10+root.left.val, ret)
        if root.right:
            self.dfs(root.right, path_sum*10+root.right.val, ret)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #method 1, DFS recrusatively
        '''
        if not root:
            return 0
        ret = []
        self.dfs(root, root.val, ret)
        return sum(ret)
        '''
        #method 2, DFS with stack
        '''
        if not root:
            return 0
        stack, ret = [(root, root.val)], 0
        while stack:
            node, cur_val = stack.pop()
            if node.left:
                stack.append((node.left, cur_val*10+node.left.val))
            if node.right:
                stack.append((node.right, cur_val*10+node.right.val))
            if not node.left and not node.right:
                ret +=cur_val
        return ret
        '''
        #method 3, BFS
        '''
        if not root:
            return 0
        q, ret = [(root, root.val)], 0
        for node, cur_val in q:
            if not node.left and not node.right:
                ret += cur_val
            if node.left:
                q.append((node.left, cur_val*10+node.left.val))
            if node.right:
                q.append((node.right, cur_val*10+node.right.val))
        return ret
        '''
        #BFS with queue
        if not root:
            return 0
        q, ret = collections.deque(), 0
        q.append((root, root.val))
        while q:
            node, pre_val = q.popleft()
            if node.left:
                q.append((node.left, pre_val*10 + node.left.val))
            if node.right:
                q.append((node.right, pre_val*10+node.right.val))
            if not node.left and not node.right:
                ret += pre_val
        return ret
# @lc code=end

