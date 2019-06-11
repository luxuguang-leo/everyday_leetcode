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
        '''
        left_profit = [0]*len(prices)
        min_left = 0
        max_left_profit = 0

        max_right = len(prices) -1
        max_right_profit = 0
        max_all = max_right_profit
        if len(prices) < 2:
            return 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_left]:
                min_left = i
            max_left_profit = max(max_left_profit, prices[i] - prices[min_left])
            left_profit[i] = max_left_profit
        max_all = left_profit[-1]
        for i in range(len(prices) -2, -1, -1):
            if prices[i] > prices[max_right]:
                max_right = i
            max_right_profit = max(max_right_profit, prices[max_right] - prices[i])
            max_all = max(max_all,max_right_profit+left_profit[i])
        return max_all
        ''' 
        #DP algo
        #fistBuy = max(firstbuy, -price[i])
        #firstSell = max(firstSell, proices[i] + firstBuy)
        #secondBuy = max(secondBuy, -prices[i] + firstSell)
        #secondSell = max(secondSell, prices[i] + secondBuy)
        if not prices:
            return 0
        #firstBuy = -prices[0]
        firstSell = 0
        #secondBuy = -prices[0]
        firstBuy = float('-inf')
        secondBuy = float('-inf')
        secondSell = 0
        for i in range(0, len(prices)):
            firstBuy = max(firstBuy, -prices[i])
            firstSell = max(firstBuy, prices[i] + firstBuy)
            secondBuy = max(secondBuy, firstSell - prices[i])
            secondSell = max(secondSell, secondBuy +prices[i])
        return secondSell

