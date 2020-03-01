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
        #@0301
        if len(nums) < 3:
            return None
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == target:#if we found three nums with its sum equal to target, definitely it will be the result
                    return val
                if abs(val - target) < abs(ans - target):#if we found smaller sum values, we update the result
                    ans = val
                elif val < target:
                    l +=1
                else:
                    r -=1
        return ans
        
# @lc code=end

