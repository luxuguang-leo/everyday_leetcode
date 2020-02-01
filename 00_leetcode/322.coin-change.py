#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        DP = [float('inf')] * (amount+1)
        DP[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    DP[i] = min(DP[i], DP[i-coin]+1)
        if DP[-1] == float('inf'):
            return -1
        return DP[-1]
        
# @lc code=end

