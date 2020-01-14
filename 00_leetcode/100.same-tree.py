#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        '''
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
        '''
        #use stack
        if not p and not q:
            return True
        if not p or not q:
            return False
        s = [(p, q)]
        while s:
            node1, node2 = s.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            s.append((node1.left, node2.left))
            s.append((node1.right, node2.right))
        return True

