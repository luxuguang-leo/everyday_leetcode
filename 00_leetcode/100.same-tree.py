#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
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
        #@0303, DFS
        '''
        if not q and not p:
            return True
        if p and q and p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
        '''
        #DFS + stack
        if not p and not q:
            return True
        stack = [(p, q)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.left))
            stack.append((l.right, r.right))
        return True
        
# @lc code=end

