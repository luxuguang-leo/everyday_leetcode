#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        partion = inorder.index(rootVal)
        root.left = self.buildTree(inorder[:partion], postorder[:partion])
        root.right = self.buildTree(inorder[partion+1:], postorder[partion:])
        return root
