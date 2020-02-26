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
        ret = []
        maj_1, cnt_1 = nums[0], 0
        maj_2, cnt_2 = nums[0], 0
        for n in nums:
            if n == maj_1:
                cnt_1 +=1
            elif n == maj_2:
                cnt_2 +=1
            elif cnt_1 == 0:
                maj_1, cnt_1 = n, 1
            elif cnt_2 == 0:
                maj_2, cnt_2 = n, 1
            else:
                cnt_1 -=1
                cnt_2 -=1
        cnt_1 = cnt_2 = 0
        for n in nums:
            if n == maj_1:
                cnt_1 +=1
            elif n == maj_2:
                cnt_2 +=1
        if cnt_1 > len(nums)//3:
                ret.append(maj_1)
        if cnt_2 > len(nums)//3:
                ret.append(maj_2)
        return ret
        
        
# @lc code=end

