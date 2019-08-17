#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#
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
        if sum == root.val and not root.left and not root.right:
            path.append(root.val)
            ret.append(path)
        if root.left:
            self.dfs(root.left, sum - root.val, path+[root.val],ret)
        if root.right:
            self.dfs(root.right, sum - root.val, path +[root.val],ret)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        if root:
            self.dfs(root, sum, [], ret)
        return ret
        

