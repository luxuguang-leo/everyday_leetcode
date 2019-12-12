#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getdepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getdepth(root.left), self.getdepth(root.right))
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #method 1
        '''
        if not root:
            return True
        leftdepth = self.getdepth(root.left)
        rightdepth = self.getdepth(root.right)
        if abs(leftdepth - rightdepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        '''
        #method 2, BFS，记录叶子节点的深度，如果两个不一层叶子节点深度差值大于1，则不平衡, 有问题！
        if not root:
            return True
        q, leaf_depth = [(root, 1)], []
        while q:
            node, level = q.pop(0)
            #记录两种情况，只有一个节点，没有节点,但还是有corner case的情况
            if not node.left or not node.right:
                leaf_depth.append(level)
                #print(leaf_depth)
                if leaf_depth[-1] - leaf_depth[0] > 1:
                    return False
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        return True
        

