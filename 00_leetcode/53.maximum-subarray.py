#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #DP[i]定义为以nums[i]为结尾的subarray的最大值
        #DP[i] = max(DP[i-1]+nums[i], nums[i])
        #然后取DP数组中最大值即可
        #由于之和前一个状态有关系，是有两个变量既可以保存前一个状态和最大长度
        '''
        if not nums:
            return 0
        DP = [0]*len(nums)
        DP[0] = nums[0]
        for i in range(1, len(nums)):
            DP[i] = max(DP[i-1]+nums[i], nums[i])
        return max(DP)
        '''
        if not nums:
            return 0
        ret = pre_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(pre_max+nums[i], nums[i])
            ret = max(ret, cur_max)
            pre_max = cur_max
        return ret
        
        
# @lc code=end

