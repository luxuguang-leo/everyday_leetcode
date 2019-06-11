#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#






























class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #here implement bisearch, the key mission is to find the part of sorted array, and use bisearch in that part
        if not nums:
            return -1
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return -1
        

