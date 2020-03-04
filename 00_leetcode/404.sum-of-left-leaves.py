#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        #recrust
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        '''
        #DFS+stack
        '''
        if not root:
            return 0
        stack = [(root, False)]
        sum = 0
        while stack:
            node, isleft = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                if isleft:
                    sum += node.val
            else:
                stack.append((node.left, True))
                stack.append((node.right, False))
        return sum
        '''
        #BFS + queue
        '''
        if not root:
            return 0
        queue = collections.deque()
        sum = 0
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and not node.left.left and not node.left.right:
                sum += node.left.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sum
        '''
        '''
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        '''
        if not root:
            return 0
        stack = [(root, False)]
        sum_val = 0
        while stack:
            node, isleft = stack.pop()
            if node:    
                if isleft and not node.left and not node.right:
                    sum_val += node.val
                else:
                    if node.left:
                        stack.append((node.left, True))
                    if node.right:
                        stack.append((node.right, False))
        return sum_val




            


        
# @lc code=end

