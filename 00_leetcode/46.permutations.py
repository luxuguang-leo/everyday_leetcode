#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, depth, res, path):
        if depth == len(path):
            res.append(list(path))
        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i]+nums[i+1:], depth, res, path)
            path.pop()

    def dfs2(self, nums, res, path):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs2(nums[:i]+nums[i+1:], res, path+[nums[i]])

        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #有两个需要控制，深度和元素
        if not nums:
            return []
        res = []
        #self.dfs(nums, len(nums), res, [])
        self.dfs2(nums, res, [])
        return res
       
        
# @lc code=end

