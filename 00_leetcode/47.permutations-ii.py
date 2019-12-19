#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res
        
# @lc code=end

