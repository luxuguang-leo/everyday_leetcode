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
        #@0303,三处可以优化
        '''
        if not preorder and not inorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        partion = inorder.index(rootVal)#O(n) -> use hashmap instead O(1)
        root.left = self.buildTree(preorder[1:partion+1],inorder[:partion]) #slicing space O(N)
        root.right = self.buildTree(preorder[partion+1:],inorder[partion+1:]) #slicing  spcae O(N)
        return root
        '''
        #优化的方法就是1.使用hashmap 2.使用索引而不是切片 但是一下方法会破坏原有的preorder数组
        if not preorder or not inorder:
            return None
        hash_map = {inorder[i]:i for i in range(len(inorder))}
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

