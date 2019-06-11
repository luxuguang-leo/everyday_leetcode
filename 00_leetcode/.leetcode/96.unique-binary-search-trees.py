#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]


