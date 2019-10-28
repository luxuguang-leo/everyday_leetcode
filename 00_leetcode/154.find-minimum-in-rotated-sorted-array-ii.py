#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []
        l, r = 0, len(nums)-1
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid +1
            else:
                r -= 1
        return nums[l]
        
# @lc code=end

