#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
class Solution(object):
    def dfs(self, candidates, target, start, level, ret):
        '''
        if target == 0 and level not in ret:
                ret.append(level)
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            self.dfs(candidates, target - candidates[i], i+1, level+[candidates[i]], ret)
        '''
        if target == 0:
            #ret.append(level)
            ret.append(list(level))
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            if i > start and candidates[i] == candidates[i-1]:
                continue
            level.append(candidates[i])
            #self.dfs(candidates, target-candidates[i], i+1,level+[candidates[i]], ret)
            self.dfs(candidates, target - candidates[i], i+1, level, ret)
            level.pop()
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        ret = []
        self.dfs(candidates, target, 0, [], ret)
        return ret
        

