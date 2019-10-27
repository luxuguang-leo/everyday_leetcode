#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #the final condation for breaking while loop is l = r + 1
        #meaning we cannot find target, in [right+1, right], a.k.a,
        #nums[right] is the last elemant we search, but failed, so we should insert 
        #target in right position, right+1 or left
        if not nums:
            return 0
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (r-l)//2 + l
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid -1
            elif target > nums[mid]:
                l = mid +1
        return l
        

