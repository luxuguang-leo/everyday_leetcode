#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #rootMax表示root为终点的path的和
    #以root为终点的和，当前的值加上左右两个子树较大的正值，如果小于0不增加
    #最终的结果却是整条路径应该是左+当前+友
    def rootMax(self, root):
        if not root:
            return float('-inf')
        l = max(0, self.rootMax(root.left))
        r = max(0, self.rootMax(root.right))
        self.ans = max(self.ans, l + r + root.val)
        return root.val + max(l, r)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS,考虑多种情况，对每一个节点左右求解取val+max(left, right, 0)
        self.ans = float('-inf')
        self.rootMax(root)
        return self.ans
        
        

