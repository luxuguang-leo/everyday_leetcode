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
        '''
        l, r = 0, len(nums)
        #find the left boundary
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] == target:
                r = mid #这里寻找左边界的时候限制右边界收缩
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
                l = mid +1#寻找右边界的时候左边界多尝试走一步
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid
        right_boundary = l - 1
        return [left_boundary, right_boundary]
        '''

        #@0229，使用同一的闭区间写法，细节也很好处理
         #其实就是找左右边界，包含了重复的数字，使用闭区间，并且注意判断限制条件
        if not nums:
            return [-1, -1]
        #标准左边界寻找
        ret = []
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                r = mid -1
            elif target < nums[mid]:
                r = mid -1
            elif target > nums[mid]:
                l = mid +1
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        ret.append(l)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                l = mid +1
            elif target > nums[mid]:
                l = mid +1
            elif target < nums[mid]:
                r = mid -1
        if r < 0 or nums[r] != target:
            return [-1, -1]
        ret.append(r)
        return ret
 
        

