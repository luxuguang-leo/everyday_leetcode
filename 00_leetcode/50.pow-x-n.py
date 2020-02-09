#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #二分降幂来求
        sign = False
        if n < 0:
            sign = True
            n = -n
        ret = 1
        while n > 0:
            if n &0x01 ==1:#没有用整除2，最终都会经过这里
                ret *= x
                n -=1
            x = x*x
            n = n//2
        if sign:
            ret = 1/ret
        return ret

        
# @lc code=end

