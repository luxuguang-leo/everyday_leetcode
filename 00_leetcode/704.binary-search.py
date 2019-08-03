#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r = 0, len(nums)-1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1
        

