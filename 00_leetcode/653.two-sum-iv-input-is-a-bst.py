#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        #inorder遍历，然后按照二分查找来计算
        '''
        if not root:
            return False
        s = [(root, False)]
        ret = []
        while s:
            node, isvisited = s.pop()
            if node:
                if isvisited:
                    ret.append(node.val)
                else:
                    s.append([node.right, False])
                    s.append([node, True])
                    s.append([node.left, False])
        #ret
        print(ret)
        for i in range(len(ret)):
            l, r = i+1, len(ret)-1
            target = k - ret[i]
            while l <= r:
                mid = l + (r-l)//2
                if target == ret[mid]:
                    return True
                elif target < ret[mid]:
                    r = mid -1
                elif target > ret[mid]:
                    l = mid +1
        return False
        '''
        #method 2,可以按照2sum思路来，每一步可以将target - k加入一个map钟，然后inorder遍历BST，
        if not root:
            return False
        m, stack = set(), [(root, False)] 
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if node.val in m:
                        return True
                    else:
                        m.add(k - node.val)
                else:
                    stack.append([node.right, False])
                    stack.append([node, True])
                    stack.append([node.left, False])
        return False
        
# @lc code=end

