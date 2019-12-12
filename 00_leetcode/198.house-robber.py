#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #DP[i],表示到底i个house所能rob的最多钱
        #DP[i] = max(DP[i-1], DP[i-2]+n[i])
        #DP[0]=nums[0]
        if not nums:
            return 0
        DP = [0]*len(nums)
        DP[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                DP[i] = max(DP[0], nums[1])
            else:
                DP[i] = max(DP[i-1], DP[i-2]+nums[i])
        return DP[-1]

        
# @lc code=end

