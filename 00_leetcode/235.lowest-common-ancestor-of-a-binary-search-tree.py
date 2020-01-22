#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #recrusive
        '''
        if not root and not q and not q:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        '''
        #non-recrusive
        '''
        if not root or not q or not p:
            return None
        while True:
            if root.val > p.val and root.val > q.val and root.left:
                root = root.left
            elif root.val < p.val and root.val < q.val and root.right:
                root = root.right
            else:
                break
        return root
        '''
        '''
        #1.dfs
        if not root or not q or not p:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        '''
        if not root or not p or not q:
            return None
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break
                #return root
        return root
        
        
        

    
# @lc code=end

