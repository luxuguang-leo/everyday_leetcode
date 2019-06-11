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
        if not prices:
            return 0
        buy, sell = -prices[0], 0
        for i in range(1, len(prices)):
            buy = max(buy, -prices[i])
            sell = max(sell, prices[i] + buy)
        return sell
        

