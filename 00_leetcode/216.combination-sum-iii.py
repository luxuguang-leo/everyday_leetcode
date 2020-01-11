#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, target,k,index, path, res):
        if k == len(path) and target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                continue
            self.dfs(nums,target-nums[i], k,i+1, path+[nums[i]], res)
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n < 0 or k < 0:
            return []
        res = []
        self.dfs(xrange(1, 10), n,k, 0, [], res)
        return res
        
# @lc code=end

