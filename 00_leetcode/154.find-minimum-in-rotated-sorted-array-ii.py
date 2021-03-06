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
        #有点类似寻找左边界
        if not nums:
            return None
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid +1
            elif nums[mid] < nums[r]:
                r = mid
            elif nums[mid] == nums[r]:
                r -=1
        return nums[l]

# @lc code=end

