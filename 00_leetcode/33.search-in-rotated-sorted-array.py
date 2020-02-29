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
        #总体想法就是, a.先确定nums[mid]在序列的前半部分还是后半部分
        #b.然后确定target在上一步骤中，根据二分查找性质进一步约束左右边界
        #所有有2x2中情况来细化，如果都不满足，返回-1
        '''
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[start]:
                if nums[mid] <= target <= nums[end]:
                    start = mid +1
                else:
                    end = mid -1
            else:
                if nums[start] <= target <= nums[mid]:
                    end = mid -1
                else:
                    start = mid +1
        return -1
        '''
        '''
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
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
        return -1
        '''
        #@0229,完全使用闭区间，在每一个有序序列中使用二分查找
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
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
        return -1


