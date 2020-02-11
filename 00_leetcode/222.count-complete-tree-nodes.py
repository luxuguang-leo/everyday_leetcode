#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self, root):
        if not root:
            return 0
        return 1 + self.getHeight(root.left)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #if heightLeft == heightRIght, left is perfert binary tree with heightLeft,
        #otherwise(heightLeft = heightRight+1) right is perfect binary tree with heightRight
        #如果左子树深度等于右子树的深度，那么左子树为满二叉树，节点为2^depth -1, 再加上根节点，所以为2^depth
        #如果左子树深度不等于右子树深度，那么右子树为满二叉树，右边部分节点可以计算可得，左边递归或者迭代获取
        '''
        if not root:
            return 0
        L = self.getHeight(root.left)
        R = self.getHeight(root.right)
        if L == R:
            return (1<<L) + self.countNodes(root.right)
        else:
            return (1<<R) + self.countNodes(root.left)
        '''
        #interactively
        '''
        def getHeight(root):
            height = 0
            while root:
                height +=1
                root = root.left
            return height
        if not root:
            return 0
        ret = 0
        while root:
            L = getHeight(root.left)
            R = getHeight(root.right)
            if L == R:
                ret += (1<<L)
                root = root.right
            else:
                ret += (1<<R)
                root = root.left
        return ret
        '''
        #二分查找？？？
                


        
        
        

        
# @lc code=end

