#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        #@0306,递归
        if not root:
            return root
        if root == p or root == q:
            return root
        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)
        if L and R:
            return root
        else:
            return L or R
        #递归方式,好难啊，总体思想是bool类型左中友三个标志，
        #如果其中一个为true，则父节点为true，如果L M R都是true，那么就是LCA节点
        #DFS
        '''
        self.ans = None
        def dfs(cur_root):
            if not cur_root:
                return False
            l = dfs(cur_root.left)
            r = dfs(cur_root.right)
            mid = False
            if cur_root == q or cur_root == p:
                mid = True
            if l + mid + r >=2:
                self.ans = cur_root
            return mid or l or r
        dfs(root)
        return self.ans
        '''
        #DFS，利用map保存父节点，等找到p,q后分别从一个(p)往回退到最终节点
        #这时候用另外一个q在结果中找，出现的话就是LCA，否则q回溯，知道在p的回溯列表中
        #'''
        parent = {root:None}
        stack = [root]
        #三者都不满足才退出，也就是p, q已经在parent中，并且p为空
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancester = set()
        while p:
            ancester.add(p)
            p = parent[p]
        while q not in ancester:
            q = parent[q]
        return q     
        #'''

        
# @lc code=end

