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
        if not root:
            return
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
        self.preorderHelper(root, ret)
        return ret
        '''
        #method 2, not easy to understand
        '''
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
        '''
        #method 3, easy to understand, why append right node first?
        #Because this is a stack, we need to visit 'left-node-right'
        #So push right node into stack first.
        stack, ret = [root], []
        while stack:
            node = stack.pop()
            if not node:
                continue
            ret.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return ret
        

