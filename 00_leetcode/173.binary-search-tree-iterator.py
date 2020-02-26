#
# @lc app=leetcode id=173 lang=python
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def pushLeft(self, root):
        if not root:
            return root
        while root:
            self.newItrator.append(root)
            root = root.left


    def __init__(self, root):
        """
        :type root: TreeNode
        """
        '''
        self.iterator = []
        self.stack = [(root, False)]
        while self.stack:
            node, visited = self.stack.pop()
            if node:
                if visited:
                    self.iterator.append(node.val)
                else:
                    self.stack.append((node.right, False))
                    self.stack.append((node, True))
                    self.stack.append((node.left, False))
        self.iterator = self.iterator[::-1]
        '''
        self.newItrator = []
        self.pushLeft(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        '''
        return self.iterator.pop()
        '''
        node = self.newItrator.pop()
        if node.right:
            self.pushLeft(node.right)
        return node.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        '''
        if self.iterator:
            return True
        else:
            return False
        '''
        return len(self.newItrator) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

