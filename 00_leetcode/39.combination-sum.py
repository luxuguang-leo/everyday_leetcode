#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    def dfs(self, candidates, target, level, ret):
        if target == 0:
            ret.append(level)
        for i in range(len(candidates)):
            if target < candidates[i]:
                return
            self.dfs(candidates[i:], target - candidates[i], level+[candidates[i]], ret)
        
    def dfs_2(self, candidates, target, start, level, ret):
        if target < 0:
            return
        if target == 0:
            #ret.append(level)
            ret.append(list(level))
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            #self.dfs_2(candidates, target - candidates[i], i, level+[candidates[i]], ret)
            level.append(candidates[i])
            self.dfs_2(candidates, target - candidates[i], i, level, ret)
            level.pop()
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #method 1, 
        '''
        if not candidates:
            return []
        candidates.sort()
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
        '''
        #method, pass index instead of slice avoiding copy
        if not candidates:
            return []
        candidates.sort()
        ret = []
        self.dfs_2(candidates, target, 0,[], ret)
        return ret


