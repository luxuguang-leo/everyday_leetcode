#
# @lc app=leetcode id=652 lang=python
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        hashdict = collections.defaultdict(list)
        def preorder(root):
            if not root:
                return "#"
            retstr = str(root.val) + preorder(root.left)+preorder(root.right)
            hashdict[retstr].append(root)
            return retstr
        preorder(root)
        ret = []
        for nodes in hashdict.values():
            if len(nodes) > 1:
                ret.append(nodes[0])
        return ret
        
# @lc code=end

