#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, start, end):
        if start > end:
            return [None]
        ret = []
        for i in range(start, end+1):
            left = self.dfs(start, i-1)
            right = self.dfs(i+1, end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ret.append(root)
        return ret

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        return self.dfs(1, n)


        

