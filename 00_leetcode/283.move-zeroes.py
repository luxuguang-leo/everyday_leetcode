#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        s, N = 0, len(nums)
        for i in range(N):
            if nums[i] != 0:
                nums[i], nums[s] = nums[s], nums[i]
                s +=1
        return nums
        '''
        #@0301
        if len(nums) <= 1:
            return nums
        zeros = 0
        for i in range(len(nums)):
            if nums[i]:
                if not nums[zeros]:
                     nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros +=1
        
# @lc code=end

