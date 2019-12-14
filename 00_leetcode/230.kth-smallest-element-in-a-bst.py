#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, ret, k):
        if not root:
            return
        #if len(ret) == k:
            #return ret
        self.dfs(root.left, ret, k)
        ret.append(root.val)
        self.dfs(root.right,ret, k)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #DFS
        '''
        ret = []
        self.dfs(root, ret, k)
        print(ret)
        return ret[k-1]
        '''
        #DFS + stack
        if not root:
            return None
        stack, ret = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ret.append(node.val)
                    if len(ret) == k:
                        return ret[-1]
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return None
                

        
# @lc code=end

