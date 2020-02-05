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
    def helper(self, root, min_val, max_val):
        if not root:
            return True
        if root.val >= max_val or root.val <= min_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)

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
        '''
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
        '''
        #DFS + stack
        '''
        stack, ret = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if ret and node.val <= ret[-1]:
                        return False
                    ret.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return True
        '''
        #其实没有必要保存之前的所有遍历元素只需要保存之前的结点的值即可所以DFS+stack可以写成
        '''
        stack, pre = [(root, False)], None
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if pre and node.val <= pre.val:
                        return False
                    pre = node
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return True
        '''
        stack, pre = [], None
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if pre and node.val <= pre.val:
                return False
            pre = node
            cur = node.right
        return True




