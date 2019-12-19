#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, start, k, path, ret):
        #if len(path) == k:
            #ret.append(path)
            #return
        if k == 0:
            ret.append(path)
            return
        for i in range(start, len(nums)):
            self.dfs(nums, i+1, k-1, path+[nums[i]], ret)
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(xrange(1, n+1), 0, k, [],ret)
        return ret
        
# @lc code=end

