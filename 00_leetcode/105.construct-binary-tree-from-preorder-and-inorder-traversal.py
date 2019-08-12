#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        partion = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1:partion+1],inorder[:partion])
        root.right = self.buildTree(preorder[partion+1:],inorder[partion+1:])
        return root

