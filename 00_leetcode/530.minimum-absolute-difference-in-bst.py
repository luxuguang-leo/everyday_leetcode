#
# @lc app=leetcode id=530 lang=python
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #1.same as normal DFS
        '''
        if not root:
            return None
        stack, pre = [], None
        ans = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if pre:
                ans = min(ans, node.val - pre.val)
            pre = node
            root = node.right
        return ans
        '''
        #2. DFS
        if not root:
            return None
        stack = [(root, False)]
        pre, ans = None, float('inf')
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if pre:
                        ans = min(ans, node.val - pre.val)
                    pre = node
                else:
                    stack.append([node.right, False])
                    stack.append([node, True])
                    stack.append([node.left, False])
        return ans
        
# @lc code=end

