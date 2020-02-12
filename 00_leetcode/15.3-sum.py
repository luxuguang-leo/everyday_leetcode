#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ret = []
        #after sorting, use 2-pointers
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    #cannot stop here, there maybe other candidates in the following array
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    #!shoud move both pointers, if not, while in deadloop
                    l +=1
                    r -=1
                elif val < 0:
                    l += 1
                else:
                    r -=1
        return ret
       