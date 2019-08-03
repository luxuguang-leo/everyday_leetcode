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
        #方法，寻找有序数列
        #1.根据 nums[mid]和 nums[start], nums[end]的关系来
        # 寻找有序数列在左半部分还是有半部分
        #情况1：  6 7 0 1 2 4 5    起始元素0在中间元素的左边
        #情况2：  2 4 5 6 7 0 1    起始元素0在中间元素的右边
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[start]:
                if nums[mid] < target <= nums[end]:
                    start = mid +1
                else:
                    end = mid -1
            else:
                if nums[start] <= target <= nums[mid]:
                    end = mid -1
                else:
                    start = mid +1
        return -1


