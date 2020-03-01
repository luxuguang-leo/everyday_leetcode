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
        #@0301,不需要从1开始
        l = 0
        for i in range(len(nums)):
            if nums[i] != nums[l]:
                l +=1
                nums[l] = nums[i]
        return l+1

        '''
        l = 0
        for i in range(1, len(nums)):
            if nums[l] != nums[i]:
                l += 1
                nums[l] = nums[i]
        return l +1
        '''

