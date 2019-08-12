#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root, ret):
        if root:
            self.preorder(root.left,ret)
            ret.append(root.val)
            self.preorder(root.right,ret)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #1
        '''
        ret = []
        if root:
            self.preorder(root, ret)
        return ret
        '''
        #2interatively, using a stack to simluation the recrusative,
        #a.push root to stack
        #b.while stack is not empty and root.left is not None, push to stack
        #c.if root.left is empty, pop stack, printf if node valus, and if root.right is not None, push to stack
        #d.return to b
        if not root:
            return []
        s, ret = [],[]
        cur = root
        while s or cur:
            while cur is not None:
                s.append(cur)
                cur = cur.left
            node = s.pop()
            ret.append(node.val)
            cur = node.right
        return ret
        
        
