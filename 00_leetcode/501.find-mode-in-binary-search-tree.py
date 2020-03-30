#
# @lc app=leetcode id=501 lang=python
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        hashmap = {}
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            hashmap[node.val] = hashmap.get(node.val, 0)+1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        max_val = max(hashmap.values())
        for key in hashmap.keys():
            if hashmap[key] == max_val:
                ret.append(key)
        return ret
        
# @lc code=end

