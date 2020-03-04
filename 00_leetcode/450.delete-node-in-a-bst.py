#
# @lc app=leetcode id=450 lang=python
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        #1. find the node
        '''
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            tmp = root.right
            minival = tmp.val
            while tmp.left:
                tmp = tmp.left
                minival = tmp.val
            root.val = minival
            root.right = self.deleteNode(root.right, minival)
        return root
        '''
        #@0304, MS's interview
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            pre = root
            miniNode = root.right
            while miniNode and miniNode.left:
                pre = miniNode
                miniNode = miniNode.left
            root.val = miniNode.val
            if pre !=root:
                pre.left = miniNode.right
            else:
                root.right = miniNode.right
        return root
            
                
                

        
# @lc code=end

