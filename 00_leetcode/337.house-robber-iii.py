#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs_dp(self, root):
        if not root:
            return (0,0)
        l = self.dfs_dp(root.left)
        r = self.dfs_dp(root.right)
        return (root.val+l[1]+r[1], max(l[0], l[1])+max(r[0], r[1]))
    def dfs(self, root, m):
        if not root:
            return 0
        if root in m:
            return m[root]
        val = 0
        if root.left:
            val += (self.dfs(root.left.left, m) + self.dfs(root.left.right, m))
        if root.right:
            val += (self.dfs(root.right.left, m) + self.dfs(root.right.right, m))
        val = max(val+root.val, self.dfs(root.left,m) + self.dfs(root.right, m))
        m[root] = val
        return val

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #TLE,DFS会超时
        '''
        if not root:
            return 0
        val = 0
        if root.left:
            val +=self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))
        '''
        #DFS,DP，第一种方法中有重叠部分，可以用记忆化递归来实现, 依然TLE../
        #'''
        m = {}
        return self.dfs(root, m)
        '''
        #DFS, DP
        #return max(self.dfs_dp(root))
        '''



        
# @lc code=end

