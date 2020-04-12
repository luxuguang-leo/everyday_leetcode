#
# @lc app=leetcode id=324 lang=python
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        
# @lc code=end

