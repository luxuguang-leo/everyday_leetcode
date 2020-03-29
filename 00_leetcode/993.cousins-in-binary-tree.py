#
# @lc app=leetcode id=993 lang=python
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        q = collections.deque([(root, 1)])
        path = collections.defaultdict(list)
        while q:
            node, level = q.popleft()
            if node.left:
                q.append([node.left, level+1])
                path[node.left.val] = [level+1, node]
            if node.right:
                q.append([node.right, level+1])
                path[node.right.val] = [level+1, node]
        if x not in path or y not in path:
            return False
        else:
            if path[x][0] == path[y][0] and path[x][1] != path[y][1]:
                return True
            else:
                return False

        
# @lc code=end

