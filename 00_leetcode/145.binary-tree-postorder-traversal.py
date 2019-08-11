#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderHelper(self, root, ret):
        if root:
            self.postorderHelper(root.left, ret)
            self.postorderHelper(root.right, ret)
            ret.append(root.val)
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #method 1
        '''
        ret = []
        if root:
            self.postorderHelper(root, ret)
        return ret
        '''
        #method 2
        #we can reverse the preorder results(DRL order)
        '''
        s, ret = [], []
        cur = root
        while s or cur:
            while cur:
                ret.append(cur.val)
                s.append(cur)
                cur = cur.right
            node = s.pop()
            cur = node.left
        ret = ret[::-1]
        return ret
        '''
        #method 3
        s, ret = [(root, False)],[]
        while s:
            node, status = s.pop()
            if node:
                if status:
                    ret.append(node.val)
                else:
                    s.append((node, True))
                    s.append((node.right, False))
                    s.append((node.left, False))
        return ret


