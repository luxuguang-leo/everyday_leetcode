#
# @lc app=leetcode id=117 lang=python
#
# [117] Populating Next Right Pointers in Each Node II
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
        #DFS with 2 queues,#amazing two deque, use another queue recording next level nodes
        '''
        if not root:
            return 
        queue, sublevel = collections.deque(), collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                sublevel.append(node.left)
            if node.right:
                sublevel.append(node.right)
            if queue:
                node.next = queue[0]
            if not queue:
            #when level node is visited..
                queue, sublevel = sublevel, queue
        return root
        '''
        #DFS, but we use three pointers, parents for parentlevel
        #childHead for next level, child for travseing nextlevel
        #                        1 -> NULL
        #                       /  \
        #parent               2  ->  3 -> NULL
        #childHead, child   /   \      \
        #                  4 ->  5 ->   6 ->NULL
        #algo. travel from top to bottom
        #algo, travel from left to right for parent level, and connect 
        #move node to childHead
        '''
        if not root:
            return
        parent = root
        childHead = child = None
        while parent:
            while parent:
                if parent.left:
                    if not childHead:
                        childHead = parent.left
                        child = parent.left
                    else:#move one step ahead in child level
                        child.next = parent.left
                        child = parent.left
                if parent.right:
                    if not childHead:
                        childHead = parent.right
                        child = parent.right
                    else:
                        child.next = parent.right
                        child = parent.right
                #go to next parent pointers
                parent = parent.next
            parent = childHead
            childHead = childHead = None
        return root
        '''
        if not root:
            return None
        q = collections.deque([root])
        subq = collections.deque()
        while q:
            node = q.popleft()
            if q:
                node.next = q[0]
            if node.left:
                subq.append(node.left)
            if node.right:
                subq.append(node.right)
            if not q:
                q, subq = subq, q
        return root
        


        
# @lc code=end

