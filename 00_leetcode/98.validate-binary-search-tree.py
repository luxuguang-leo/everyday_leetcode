#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #method 1
        '''
        return self.helper(root, float('-inf'), float('inf'))
        '''
        #method 2, inorder and judge if the result is ordered
        ##
        s, ret = [], []
        cur = root
        while s or cur:
            while cur:
                s.append(cur)
                cur = cur.left
            node = s.pop()
            #ret.append(node.val)
            if ret and node.val <= ret[-1]:
                return False
            ret.append(node.val)
            cur = node.right
        return True



