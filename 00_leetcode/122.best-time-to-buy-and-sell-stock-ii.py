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
        # buy = max(buy, sell - prices[i])
        # sell = max(sell, buy + prices[i])
        #这里不再约束次数，所以买的时候需要考虑卖的因素
        if len(prices) <= 1:
            return 0
        buy = - prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])
        return sell
        

