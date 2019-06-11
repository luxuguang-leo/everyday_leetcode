#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (29.41%)
# Total Accepted:    286K
# Total Submissions: 964.2K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#
class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end -1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #space complicity O(n), use another list, (i+k)%n -> i
        '''
        nums_cp = nums[:]
        for i in range(len(nums)):
            ind = (i+k)%len(nums)
            nums[ind] = nums_cp[i]
        return nums
        '''
        #O(1) complixity
        cnt = len(nums)
        i= 0
        ind = (i+k)%cnt
        while  ind !=  0:
            nums[i], nums[ind] = nums[ind], nums[i]
            i = ind
            ind = (i+k)%cnt
        nums[ind], nums[0] = nums[0], nums[ind]
        return nums
        
        #flip 3 times
        '''
        l = len(nums)
        k = k %l
        self.reverse(nums, 0, l - k -1)
        self.reverse(nums, l-k , l- 1)
        self.reverse(nums, 0, l -1)
        '''

