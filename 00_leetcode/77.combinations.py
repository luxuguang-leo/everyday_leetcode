#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, k, i, res, path):
        if len(path) == k:
            res.append(path)
        for i in range(i, len(nums)):
            self.dfs(nums, k, i+1,res, path+[nums[i]])

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 0 or k <= 0:
            return []
        res = []
        self.dfs(xrange(1, n+1), k, 0, res, [])
        return res
   
        
# @lc code=end

