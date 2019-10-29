#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) -1
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] < nums[mid+1]:
                l = mid +1
            else:
                r = mid
        return l
        
# @lc code=end

