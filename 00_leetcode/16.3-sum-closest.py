#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum_val = sum(nums[:3])
        nums.sort()
        for i in range(len(nums) -2):
            start, end = i+1, len(nums)-1
            while start < end:
                val = nums[i] + nums[start] + nums[end]
                if abs(val - target) < abs(sum_val - target): 
                    sum_val = val
                if val < target:
                    start += 1
                else:
                    end -= 1
        return sum_val
            
        

