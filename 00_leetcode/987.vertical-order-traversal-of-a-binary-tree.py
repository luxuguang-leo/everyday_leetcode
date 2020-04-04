#
# @lc app=leetcode id=987 lang=python
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = collections.deque()
        q.append([root, 0])
        cols = collections.defaultdict(list)
        while q:
            tmp = collections.defaultdict(list)
            for _ in range(len(q)):
                node, x = q.popleft()
                tmp[x].append(node.val)
                if node.left:
                    q.append((node.left, x-1))
                if node.right:
                    q.append((node.right, x+1))
            #对临时的list需要排序后放到最后的hashmap中，否则相同的值并没有按照值大小排列
            for n in tmp:
                cols[n].extend(sorted(tmp[n]))
        return [cols[c] for c in sorted(cols.keys())]
        
# @lc code=end

