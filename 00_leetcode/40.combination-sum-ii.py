#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, target, start, res, path):
        if target == 0:
            res.append(path)
        for i in range(start, len(nums)):
            if nums[i] > target:
                continue
            if i > start and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target - nums[i], i+1, res, path+[nums[i]]) 
   
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return [[]]
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res
        
# @lc code=end

