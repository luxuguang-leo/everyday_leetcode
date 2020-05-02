#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque([root])
        ret = []
        while q:
            path = []
            for _ in range(len(q)):
                node = q.popleft()
                path.append(node.val)
                for child in node.children:
                    q.append(child)
            ret.append(path)
        return ret
        
# @lc code=end

