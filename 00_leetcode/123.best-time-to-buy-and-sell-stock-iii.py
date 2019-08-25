#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #4 states
        #firstBuy = max(firstBuy, -prices[i])
        #firstSell = max(firstSell, firstBuy + prices[i])
        #secondBuy = max(secondBuy, firstSell - prices[i])
        #secondSell = max(secondSell, secondBuy + prices[i])
        if len(prices) <= 1:
            return 0
        firstBuy = - 0xFFFFFFFF
        firstSell = 0
        secondBuy = -0xFFFFFFFF
        secondSell = 0
        for i in range(0, len(prices)):
            firstBuy = max(firstBuy, -prices[i])
            firstSell = max(firstSell, firstBuy + prices[i])
            secondBuy = max(secondBuy, firstSell - prices[i])
            secondSell = max(secondSell, secondBuy + prices[i])
        return secondSell

