#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        for i in range(1, len(nums)):
            if nums[l] != nums[i]:
                l += 1
                nums[l] = nums[i]
        return l +1

