#
# @lc app=leetcode id=515 lang=python
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root
        q = collections.deque([root])
        ret = []
        while q:
            max_val = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                if node.val > max_val:
                    max_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ret.append(max_val)
        return ret
        
# @lc code=end

