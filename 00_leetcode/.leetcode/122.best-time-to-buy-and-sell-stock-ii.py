#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy = -prices[0]
        sell = 0
        for i in range(len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, prices[i] + buy)
        return sell
