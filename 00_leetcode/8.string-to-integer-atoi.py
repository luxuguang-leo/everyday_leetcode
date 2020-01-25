#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip(" ")
        ret = 0
        sign = 1
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        for ch in s:
            val = ord(ch) - ord('0')
            if 0 <= val <= 9:
                ret = ret*10 + val
            else:
                break
        ret *= sign
        '''
        if ret >= 2**31 -1:
            return 2**31 -1
        if ret <= -2**31:
            return -2**31
        '''
        #return max(-2**31, min(ret, 2**31-1))
        return min(2**31-1, max(ret, -2**31))
       

        

        
# @lc code=end

