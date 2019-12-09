#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = 0 - x
        ret = 0
        while x > 0:
            digit = x%10
            x = x/10
            ret = ret*10 + digit
        if ret > 0x7FFFFFFF:
            return 0
        return sign * ret
        
# @lc code=end

