#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """



















        l , r = 0 , len(nums)-1
        while l <=r: 
            mid = l + (r-l)//2
            if target == nums[mid]:
                r = mid -1
            elif target < nums[mid]:
                r = mid -1
            else:
                l = mid +1
        if l == len(nums):
            return [-1, -1]
        l1, r1 = 0, len(nums) -1
        while l1 <= r1:
            mid = l1 + (r1-l1)//2
            if target == nums[mid]:
                l1 = mid +1
            elif target > nums[mid]:
                l1 = mid +1
            else:
                r1 = mid -1
        if l == r1:
            return [-1, -1]
        else:
            return [l, r1]
        











    
        

