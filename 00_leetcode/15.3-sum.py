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
            s, e = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while s < e:
                val = nums[i] + nums[s] + nums[e]
                if val == 0:
                    ret.append([nums[i], nums[s], nums[e]])
                    #cannot stop here, there maybe other candidates in the following array
                    while s < e and nums[s] == nums[s+1]:
                        s +=1
                    while s < e and nums[e] == nums[e-1]:
                        e -=1
                    s +=1
                    e -=1
                elif val < 0:
                    s += 1
                else:
                    e -=1
        return ret
        
# @lc code=end

