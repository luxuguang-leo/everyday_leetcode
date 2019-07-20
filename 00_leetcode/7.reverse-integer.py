#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = 0 - x
        else:
            sign = 1
        ret = 0
        while x > 0:
            dig = x%10
            x = x/10
            ret = ret*10+dig
        if ret > 0x7FFFFFFF:
            return 0
        return sign*ret

        #1) 123
        #dig = 3
        #x = 12
        #ret = 3

        #12 
        #dig = 2
        #x = 1
        #result = 3*10 + 2 = 32

        #2) 1
        #dig = 1
        #x = 0
        #result = 320+1 = 321

        

        

