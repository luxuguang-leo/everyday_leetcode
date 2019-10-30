#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #动态规划方法，f(n)表示以nums[n]为最后一个的最长子序列
        #f(i) = max(f(j)) +1 if nums[j] < nums[i]
        if not nums:
            return 0
        dp = [1]*len(nums)
        ret = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                ret = max(ret, dp[i])
        return ret
# @lc code=end

