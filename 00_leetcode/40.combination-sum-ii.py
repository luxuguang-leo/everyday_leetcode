#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return [[]]
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res
        
# @lc code=end

