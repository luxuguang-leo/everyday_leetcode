#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == None or len(nums) == 0:
            return []
        maj_idx1= maj_idx2 = 0
        cnt1 = cnt2 = 0
        for i in range(len(nums)):
            if nums[maj_idx1] == nums[i]:
                cnt1 +=1
            elif nums[maj_idx2] == nums[i]:
                cnt2 +=1
            elif cnt1 == 0:
                maj_idx1 = i
                cnt1 =1
            elif cnt2 == 0:
                maj_idx2 =i
                cnt2 =1
            else:
                cnt1 -=1
                cnt2 -=1
        cnt1 = cnt2 =0
        ret = []
        for i in range(len(nums)):
            if nums[i] == nums[maj_idx1]:
                cnt1 +=1
            elif nums[i] == nums[maj_idx2]:
                cnt2 +=1
        if cnt1 > len(nums)/3:
            ret.append(nums[maj_idx1])
        if cnt2 > len(nums)/3:
            ret.append(nums[maj_idx2])
        return ret
        
        
# @lc code=end

