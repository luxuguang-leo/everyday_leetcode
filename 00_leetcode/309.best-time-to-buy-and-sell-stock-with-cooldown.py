#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #DP，和之前的区别在于买入前，需要等过了冷冻期，也就是buy[i]和sell[i-2]有关系
        #buy[i] = max(buy[i-1], sell[i-2] -price[i])
        #sell[i] = max(sell[i-1], buy[i-1] + price[i])
        if len(prices) <= 1:
            return 0
        N = len(prices)
        buy = [0]*N
        sell = [0]*N
        buy[0]=-prices[0]
        #buy[1] = ，表示第二天买，为取最大值，应该取max(-price[0], -price[1])
        for i in range(1, N):
            if i > 1:
                buy[i] = max(buy[i-1], sell[i-2] - prices[i])
                #sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            else:
                buy[i] = max(buy[i-1], -prices[i])
                #sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        return sell[-1]


        
# @lc code=end

