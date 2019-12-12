#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0
        if N <= 2:
            return max(nums)
        def rob_range(nums):
            if len(nums) <= 2:
                return max(nums)
            N = len(nums)
            dp = [0]*N
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(1, len(nums)):
                if i == 1:
                    dp[i] = max(dp[0], nums[1])
                else:
                    dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]
        return max(rob_range(nums[0:N-1]), rob_range(nums[1:N])) 


# @lc code=end

