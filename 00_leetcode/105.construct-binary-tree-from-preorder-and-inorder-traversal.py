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
        #take the index carefully
        #@0303
        '''
        if not preorder and not inorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        partion = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1:partion+1],inorder[:partion])
        root.right = self.buildTree(preorder[partion+1:],inorder[partion+1:])
        return root
        '''
        if not preorder or not inorder:
            return None
        hash_map = {}
        for i, node in enumerate(inorder):
            hash_map[node] = i
        def recv(start, end):
            if start > end:
                return None
            rootVal = preorder.pop(0)
            root = TreeNode(rootVal)
            index = hash_map[rootVal]
            root.left = recv(start, index-1)
            root.right = recv(index+1, end)
            return root
        return recv(0, len(inorder)-1)

