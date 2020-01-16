#
# @lc app=leetcode id=99 lang=python
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.pre and root.val < self.pre.val:
            if not self.first:
                self.first = self.pre
            #1.不应该用elif判断，因为有可能只存在一对不符合BST的序列，应该每一次都记录second的值
            #2.记录的是tree的结点而不是值，最终交换的是值
            '''
            elif not self.second:
                self.second = root
            '''
            self.second = root
        self.pre = root
        self.dfs(root.right)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root
# @lc code=end

