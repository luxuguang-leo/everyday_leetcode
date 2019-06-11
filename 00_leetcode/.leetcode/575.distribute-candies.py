#
# @lc app=leetcode id=575 lang=python
#
# [575] Distribute Candies
#
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if not candies:
            return 0
        return min(len(set(candies)), len(candies)/2)

