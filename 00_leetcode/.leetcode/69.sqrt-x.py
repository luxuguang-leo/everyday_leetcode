#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        











        l, r = 0, x-1
        while l <=r:
            mid = l + (r-l)//2
            if mid*mid <= x <= (mid+1)*(mid+1):
                return mid
            elif
                

