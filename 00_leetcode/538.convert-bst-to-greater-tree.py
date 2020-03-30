#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #对右，中，左遍历,中序遍历逆序处理
        '''
        self.ans = 0
        def reverseInorder(root):
            if not root:
                return None
            reverseInorder(root.right)
            self.ans += root.val
            root.val = self.ans
            reverseInorder(root.left)
            return root
        return reverseInorder(root)
        '''
        self.ans = 0
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    self.ans += node.val
                    node.val = self.ans
                else:
                    stack.append([node.left, False])
                    stack.append([node, True])
                    stack.append([node.right, False])
        return root

        
# @lc code=end

