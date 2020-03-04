#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        #层次遍历？然后级联
        '''
        if not root:
            return root
        queue,ret = collections.deque(),[]
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left and node.right:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        '''
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root

            
                
                
        
# @lc code=end

