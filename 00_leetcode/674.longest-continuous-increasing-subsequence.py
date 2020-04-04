#
# @lc app=leetcode id=674 lang=python
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        ret, cnt = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cnt +=1
            else:
                cnt = 1
            ret = max(ret, cnt)   
        return ret     
# @lc code=end

