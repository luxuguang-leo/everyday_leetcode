#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
class Solution(object):
    def dfs(self, nums, start, path, ret):
        ret.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i +1, path+[nums[i]], ret)
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ret = []
        self.dfs(nums, 0, [], ret)
        return ret

