#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
class Solution(object):
    def dfs(self, nums, start, path, ret):
        '''
        if path not in ret:
            ret.append(path)
        '''
        ret.append(path)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], ret)
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        ret = []
        self.dfs(nums, 0, [], ret)
        return ret
        

