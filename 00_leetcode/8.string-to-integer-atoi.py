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
        #elimate whitespace from left
        s = str.strip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        ret = 0
        for i in range(len(s)):
            val = ord(s[i])-ord("0")
            if val < 0 or val > 9:
                break
            ret = ret*10 + val
        ret = ret*sign
        if ret > 2147483647:
            return 2147483647
        #if ret < -sys.maxint-1:
            #return -sys.maxint-1
        if ret < -2147483648:
            return -2147483648
        return ret


        

        
# @lc code=end

