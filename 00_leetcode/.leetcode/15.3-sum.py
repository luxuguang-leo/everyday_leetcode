#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.68%)
# Total Accepted:    516.1K
# Total Submissions: 2.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #divide i 2sums
        res = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            map_test = {}
            tmp_list = []
            for j in range(i+1, l):
                if nums[j] == nums[j-1]:
                    continue
                if nums[j] not in map_test:
                    map_test[0-nums[i] - nums[j]] = j
                else:
                    tmp_list = [nums[i], nums[j], nums[map_test[nums[j]]]]
                    if tmp_list not in res:
                        res.append(tmp_list)
        return res

