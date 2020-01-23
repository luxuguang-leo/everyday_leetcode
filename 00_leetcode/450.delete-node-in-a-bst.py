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
        if not root:
            return None
        if key > root.val:#should delete in the right subtree 
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:#should delete in the left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            #find the smallest val in the right subtree
            pre = root
            miniNode = root.right
            while miniNode and miniNode.left:
                pre = miniNode
                miniNode = miniNode.left
            root.val = miniNode.val
            #then delete miniNode, but should take care whether 
            if pre != root:#if the right subtree have left tree
                pre.left = miniNode.right
            else:
                pre.right = miniNode.right
        return root
            
                
                

        
# @lc code=end

