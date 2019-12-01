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
        #DP问题，
        #一般可得DP[11] = min(DP[10], DP[9], DP[6]) +1
        #DP[10] = min(DP[9], DP[8], DP[5]) +1
        DP = [float("inf")]*(amount+1)
        DP[0] = 0#表示凑够0不需要任何数量的钱
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    DP[i] = min(DP[i], DP[i-coins[j]]+1) 
        if DP[-1] <= amount:
            return DP[-1]
        else:
            return -1
        
# @lc code=end

