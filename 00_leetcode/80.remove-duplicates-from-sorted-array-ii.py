#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        s = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[s] or nums[i] == nums[s] and nums[i] != nums[s-1]:
                s +=1
                nums[s] = nums[i]
        return s+1
        
# @lc code=end

