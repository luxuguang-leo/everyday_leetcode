#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        #考虑极限情况，nums[l], nums[mid], nums[r] 相等在一条直线上，无法区分，别的情况
        #为何不考虑，别的情况可以区分有序数列，所以需要将前面水平的一段剔除掉, 当mid在后半段，则左边界会往右，nums[l]最终会超过num[mid]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:
                l+=1
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return False
# @lc code=end

