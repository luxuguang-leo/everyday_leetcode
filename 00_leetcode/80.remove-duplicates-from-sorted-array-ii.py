#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #similar to previous #26, use two pointers, slow and fast
        #key is to find when to replace the previous elements
        #for #26, just need to satify A[fast] != A[slow]
        #but for #80, we need to compare A[fast] != A[slow] or
        #A[fast] == A[slow] and A[fast] != A[slow -1]
        if len(nums) <= 2:
            return len(nums)
        slow = 1
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow] or nums[fast] == nums[slow] and nums[fast] != nums[slow-1]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
        

