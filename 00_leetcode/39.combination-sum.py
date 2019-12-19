#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    def dfs2(self, nums, target, start, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
        for i in range(start, len(nums)):
            self.dfs2(nums,target-nums[i], i, path+[nums[i]], ret)

    def dfs(self, nums, target, level, ret):
        if len(ret) < level +1:
            level_list = []
        if target == 0:
            ret.append(level_list)
        for i in range(len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target - nums[i], i+1, ret)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #dfs
        '''
        if not candidates:
            return []
        ret = []
        self.dfs(candidates, target, 0, ret)
        return ret
        '''
        if not candidates:
            return [[]]
        ret = []
        #candidates.sort()
        self.dfs2(candidates, target, 0, [], ret)
        return ret
        

