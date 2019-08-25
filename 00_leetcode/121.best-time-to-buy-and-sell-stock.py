#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #method 1
        '''
        if len(prices) <=1:
            return 0
        max_profit = 0
        min_val = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_val)
            min_val = min(min_val, prices[i])
        return max_profit
        '''

        #method 2, DP, 
        #buy  -> -prices[i]
        #sell -> prices[i]
        #状态，买 buy = max(buy, -prices[i])
        #状态，卖 sell = max(sell, buy + prices[i])
        if len(prices) <= 1:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy = max(buy, -prices[i])
            sell = max(sell, buy + prices[i])
        return sell
        

