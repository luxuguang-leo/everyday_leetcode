#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #类似于26进制数
        ret = ''
        while n > 0:
            ret = chr((n-1)%26+ 65) + ret
            n = (n-1)/26
        return ret
            
        

