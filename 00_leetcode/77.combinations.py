#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
class Solution(object):
    def dfs(self, nums, k, level, level_list, ret):
        if k == 0:
            ret.append(level_list)
            return 
        for i in range(level, len(nums)):
            self.dfs(nums, k-1, i+1, level_list+[nums[i]], ret)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n == 0:
            return []
        ret = []
        self.dfs(range(1, n+1), k, 0, [],ret)
        return  ret
        