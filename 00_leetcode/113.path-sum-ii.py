#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, sum, path, ret):
        if not root:
            return
        if not root.left and not root.right and sum==0:
            ret.append(path)
            return 
        if root.left:
            self.dfs(root.left, sum-root.left.val, path+[root.left.val],ret)
        if root.right:
            self.dfs(root.right, sum-root.right.val, path+[root.right.val],ret)
        #return ret
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        #DFS with recrusatively
        '''
        if not root:
            return []
        ret = []
        self.dfs(root, sum-root.val, [root.val], ret)
        return ret
        '''
        #DFS with stack
        '''
        if not root:
            return []
        stack = [(root, root.val, [root.val])]
        ret = []
        while stack:
            node,cur_sum, path = stack.pop()
            if node.left:
                stack.append((node.left, cur_sum + node.left.val, path+[node.left.val]))
            if node.right:
                stack.append((node.right, cur_sum + node.right.val, path+[node.right.val]))
            if not node.left and not node.right and cur_sum == sum:
                ret.append(path)
        return ret
        '''
        #DFS @0303
        if not root:
            return []
        ans = []
        stack = [(root, root.val, [root.val])]
        while stack:
            node, cur_sum, path = stack.pop()
            if not node.left and not node.right and cur_sum == sum:
                ans.append(path)
            if node.left:
                stack.append((node.left, cur_sum + node.left.val, path+[node.left.val]))
            if node.right:
                stack.append((node.right, cur_sum + node.right.val, path+[node.right.val]))
        return ans

# @lc code=end

