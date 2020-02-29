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
        #@0229,使用二分指数来缩减运算规模，一个技巧就是对x的处理
         #由于n是整数
        #1.n==0, 返回1
        #2.n < 0 最终用1被除即可
        #3.n > 0 
        #3.1 n%2 == 0偶数，分解为x**(n//2)
        #3.2 n%2 == 1奇数，分解为x*x**(n-1)
        if n == 0:
            return 1
        sign = True
        if n < 0:
            n = -n
            sign = False
        ret = 1
        while n > 0:
            if n&0x01:#奇数
                ret *= x
                n -= 1
            x = x*x
            n //= 2
        if not sign:
            ret = 1/ret
        return ret
        
# @lc code=end

