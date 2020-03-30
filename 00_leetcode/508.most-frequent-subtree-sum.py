#
# @lc app=leetcode id=508 lang=python
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []
        m = collections.defaultdict(int)
        def cur_sum(root):
            if not root:
                return 0
            val = root.val + cur_sum(root.left) + cur_sum(root.right)
            m[val] +=1
            return val
        cur_sum(root)
        mx = max(m.values())
        for key in m.keys():
            if m[key] == mx:
                ret.append(key)
        return ret
        
# @lc code=end

