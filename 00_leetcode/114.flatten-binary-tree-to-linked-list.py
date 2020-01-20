#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        #preorder
        #supporse left part has been flattened
        if not root:
            return root
        while root:
            if root.left:
                self.flatten(root.left)
                node1 = root.left
                #find the last node in the already-flattened left tree
                while node1 and node1.right:
                    node1 = node1.right
                node1.right = root.right
                root.right, root.left = root.left, None
            root = root.right
        return root
# @lc code=end

