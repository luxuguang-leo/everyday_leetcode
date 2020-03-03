#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,start, end):
        if start > end:
            return [None]
        ret = []
        for i in range(start, end+1):
            L = self.dfs(start, i-1)
            R = self.dfs(i+1, end)
            for left in L:
                for right in R:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ret.append(root)
        return ret

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #DFS. @0302
        if n < 1:
            return []
        return self.dfs( 1, n)
        
# @lc code=end

