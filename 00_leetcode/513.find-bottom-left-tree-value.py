#
# @lc app=leetcode id=513 lang=python
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return root
        q = collections.deque([root])
        ret_val = None
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    ret_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ret_val
        
# @lc code=end

