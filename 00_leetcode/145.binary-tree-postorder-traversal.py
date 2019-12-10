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
    def dfs(self, root, ret):
        if not root:
            return
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
        dfs(root, ret)
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
        stack, ret = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                else:
                    ret.append(node.val)
        return ret


