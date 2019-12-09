#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor < 0 and dividend < 0 or divisor > 0 and dividend > 0:
            sign = True
        else:
            sign = False
        digits = 0
        #find how many shitfs, 2^n*(1 or 0) +2^(n-1)*(1 or 0) 
        dividend, divisor = abs(dividend), abs(divisor)
        while divisor <= dividend:
            divisor <<=1
            digits +=1
        divisor >>= digits
        digits -=1
        ret = 0
        while digits >= 0:
            if dividend >= divisor << digits:
                dividend -= divisor << digits
                ret += 1<<digits
            digits -=1
        if sign:
            return min(2147483647, ret)
        else:
            return max(-2147483648, -ret)
# @lc code=end

