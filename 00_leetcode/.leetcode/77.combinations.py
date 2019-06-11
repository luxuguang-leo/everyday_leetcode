#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
class Solution(object):













    def dfs(self, n, k, res, level,level_list):
        if n == 0 and level == k:
            res.append(level_list)
            return 
        elif n < 0:
            return
        else:
            for i in range(1, n):
                self.dfs(n - i, k, res, level+1, level_list+[i])



    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #n and k, seems little tricky
        #need DFS?
        if n < k:
            return [[]]
        res = []
        self.dfs(n, k, res, 0,[])
        return res
