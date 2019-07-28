#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        ret = 0
        #tmp = 121, ret =0
        #tmp = 12, ret = 12
        #tmp = 1,ret = 120
        #tmp = 0, ret = 121
        while tmp > 0:
            ret = ret*10 + tmp%10
            tmp = tmp/10
        if ret == x:
            return True
        else:
            return False
        

