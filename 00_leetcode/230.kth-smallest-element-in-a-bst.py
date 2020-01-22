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
    def dfs2(self, root):
        if not root:
            return 
        self.dfs2(root.left)
        self.k -=1
        if(self.k == 0):
            self.ret = root.val
            return self.ret
        self.dfs2(root.right)
        
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
        '''
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
        '''
        #recrusatively
        '''
        if not root:
            return root
        self. k = k
        self.ret = None
        self.dfs2(root)
        return self.ret
        '''
        #interative
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        #return node.val
                

        
# @lc code=end

