#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, sum):
        #注意DFS和pathSum区别，DFS表示一定选root这个结点组成最终的结果
        if not root:
            return 0
        #if root in self.hashmap:
            #return self.hashmap[root]
        ans_cnt = 0
        if root.val == sum:
            ans_cnt +=1
        ans_cnt += self.dfs(root.left, sum-root.val)
        ans_cnt += self.dfs(root.right, sum-root.val)
        self.hashmap[root] = ans_cnt
        #return ans_cnt
        return self.hashmap[root]
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #1.对于每一个结点有两种选择，选或者不选
        #2.注意题目是从上到下的，不是左右皆选的类似，必须从root到结点
        if not root:
            return 0
        self.hashmap = {}
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.dfs(root, sum)
        
# @lc code=end

