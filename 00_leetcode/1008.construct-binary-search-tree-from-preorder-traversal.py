#
# @lc app=leetcode id=1008 lang=python
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        #O(N^2), why cause bisect in unordered array
        '''
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        idx = bisect.bisect(preorder, preorder[0])
        root.left = self.bstFromPreorder(preorder[1:idx])
        root.right = self.bstFromPreorder(preorder[idx:])
        return root
        '''
        #O(NlgN), why because bisect in 
        '''
        def dfs(left, right):
            if left == right:
                return None
            root = TreeNode(preorder[left])
            idx = bisect.bisect(preorder, preorder[left], left, right)
            root.left = dfs(left+1, idx)
            root.right = dfs(idx, right)
            return root
        if not preorder:
            return None
        return dfs(0, len(preorder))
        '''
        #O(N), it's BST, first find the root, travel throught the list:
        #then 2 cases:1. smaller than stack's last node's value, left node
        #2.larger, pop stack till find a large node
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            if val < stack[-1].val:
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < val:
                    last = stack.pop()
                last.right = TreeNode(val)
                stack.append(last.right)
        return root

                
        
# @lc code=end

