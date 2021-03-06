#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        if len(nums) <=1:
            return nums
        #左右两个数组
        left, right = [1]*len(nums), 1
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            left[i] *= right
        return left
        '''
        #分别从两个方向求乘积，放到两个数组中，最终两边相乘就得到结果
        #因为最终结果是也是要乘，所以需要秩序保存在一个数组里面即可
        ret = [1]*len(nums)
        #left ->right
        for i in xrange(1, len(nums)):
            ret[i] = ret[i-1]*nums[i-1]
        tmp =1
        for j in xrange(len(nums)-2, -1, -1):
            tmp *= nums[j+1]
            ret[j] *= tmp
        return ret
        
# @lc code=end

