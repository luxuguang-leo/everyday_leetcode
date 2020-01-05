#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        nums.sort()
        sum_val = sum(nums[:3])
        for i in range(len(nums)-2):
            s, e = i+1, len(nums)-1
            while s < e:
                val = nums[i] + nums[s] + nums[e]
                if abs(val - target) < abs(sum_val - target):
                    sum_val = val
                elif val < target:
                    s +=1
                else:
                    e -=1
        return sum_val
        
# @lc code=end

