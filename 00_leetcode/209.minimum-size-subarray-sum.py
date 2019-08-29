#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        sum = 0
        min_len = float('inf')
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_len = min(min_len, i - left +1)
                sum -= nums[left]
                left += 1
        if min_len == float('inf'):
            return 0
        return min_len
        

