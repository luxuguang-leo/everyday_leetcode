#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (43.38%)
# Total Accepted:    342.9K
# Total Submissions: 787.9K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #soluction 1, brutal 
        '''
        max_area = 0
        for i in range(1, len(height)):
            for j in range(0, i):
                max_area = max(max_area, (i-j)*min(height[i], height[j]))
        return max_area
        '''
        #剪枝，减小无用判断
        '''
        max_area = 0
        for i in range(1, len(height)):
            if height[i] == 0:
                continue
            max_ind = i - max_area/height[i]
            for j in range(0, i):
                if j < max_ind:
                    max_area = max(max_area, (i-j)*min(height[i], height[j]))
        return max_area
        '''
        #依然无法通过大数组， 
        left, right = 0, len(height)-1
        max_area = 0
        while left <= right:
            max_area = max(max_area, (right - left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

