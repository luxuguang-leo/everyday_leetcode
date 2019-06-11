#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):

    def dfs(self, candidates, target, level, res):
        level_res = []
        if target = 0:
            return res.append(level_res)
        for i in range(len(candidates)):
            if candidates

            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        dfs(self, candidates, target, 0 ,res)
        return res
        

