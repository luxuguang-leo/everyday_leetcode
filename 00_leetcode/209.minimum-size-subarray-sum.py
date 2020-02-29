#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #大概思路就是欢滑动窗口，小于s的时候向右滑动,一边累计sum值
        #当sum大于s的时候就停止滑动，然后左边界收缩，知道小于s
        #如果中间等于s则更新窗口长度
        #不知道为啥打上binary-search标签
        '''
        if not nums:
            return 0
        l, r, sum_val = 0, 0, 0
        min_len = float('inf')
        while r < len(nums):
            sum_val += nums[r]
            while sum_val >= s:
                min_len = min(min_len, r-l+1)
                sum_val -=nums[l]
                l +=1
            r += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len
        '''
        if not nums:
            return 0
        sum_val =  l = 0
        window = float('inf')
        for i in range(len(nums)):
            sum_val += nums[i]
            while sum_val >= s:
                window = min(window, i - l +1)
                sum_val -=nums[l]
                l +=1
        if window == float('inf'):
            return 0
        else:
            return window

