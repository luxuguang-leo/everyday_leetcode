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
        s, N = 0, len(nums)
        for i in range(N):
            if nums[i] != 0:
                nums[i], nums[s] = nums[s], nums[i]
                s +=1
        return nums
        
# @lc code=end

