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
        if not root:
            return 0
        def getHeight(root):
            if not root:
                return 0
            height = 0
            while root:
                height +=1
                root = root.left
            return height
        numNodes = 0
        while root:
            L = getHeight(root.left)
            R = getHeight(root.right)
            if L == R:
                numNodes += (1<<L)
                root = root.right
            else:
                numNodes += (1<<R)
                root = root.left
        return numNodes

        
        
        

        
# @lc code=end

