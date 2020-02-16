#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
class Solution(object):
    def dfs(self, nums, res, path):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], res, path+[nums[i]])
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), res, [])
        return res

