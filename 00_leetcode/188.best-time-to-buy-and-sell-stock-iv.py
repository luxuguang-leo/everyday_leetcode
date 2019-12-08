#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #当k超过N//2的时候相当于不限制次数，退化为任意买卖次数的问题
        #当k小于N//2的时候相当于状态转移方程只迭代k次
        N = len(prices)
        if N <= 1:
            return 0
        ret = 0
        if k >= N//2:
            for i in range(1, N):
                ret +=  max(0, prices[i]-prices[i-1])
            return ret 
        buy = [0]*N
        sell = [0]*N
        buy[0] = prices[0]
        for _ in range(k): # run k times
            for i in range(1, N):
                buy[i] = min(buy[i-1], prices[i]-buy[i]) # renew buy price
                sell[i] = max(sell[i-1], prices[i]-buy[i]) # renew accumulate sell price
            buy = [prices[0]]+sell[0:] # new shift
            sell = [0]*N# initialize for next k
        return buy[-1] # Beca
        
# @lc code=end

