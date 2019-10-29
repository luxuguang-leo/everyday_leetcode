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
        l, r = 0, len(nums)
        #find the left boundary
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] == target:
                r = mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid +1
        if l == len(nums):
            left_boundary = -1
        elif nums[l] == target:
            left_boundary = l
        else:
            left_boundary = -1
        if left_boundary == -1:
            return [-1, -1]
        #find right boundary
        l, r = 0, len(nums)
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] == target:
                l = mid +1
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid
        right_boundary = l - 1
        return [left_boundary, right_boundary]
 
        

