#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderHelper(self, root, ret):
        if root:
            ret.append(root.val)
            self.preorderHelper(root.left, ret)
            self.preorderHelper(root.right, ret)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #method 1
        '''
        ret = []
        if root:
            self.preorderHelper(root, ret)
        return ret
        '''
        #method 2
        s, ret = [], []
        cur = root
        while s or cur:
            while cur:
                ret.append(cur.val)
                s.append(cur)
                cur = cur.left
            node = s.pop()
            cur = node.right
        return ret
        

