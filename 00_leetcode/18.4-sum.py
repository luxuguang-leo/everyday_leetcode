#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #@0301
        if len(nums) < 4:
            return []
        ret = set()
        nums.sort()
        for i in range(len(nums)-2):
            newtarget = target - nums[i]
            for j in range(i+1, len(nums)-2):
                re_target = newtarget - nums[j]
                l, r = j +1, len(nums)-1
                while l < r:
                    val = nums[l] + nums[r]
                    if val == re_target:
                        ret.add((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -=1
                        l +=1
                        r -=1
                    elif val < re_target:
                        l +=1
                    else:
                        r -=1
        return ret
        
# @lc code=end

