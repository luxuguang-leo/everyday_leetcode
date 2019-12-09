#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#

# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ""
        def str2num(s):
            ret = 0
            for i in range(0, len(s)):
                val = ord(s[i]) - ord('0')
                ret = ret * 10 + val
            return ret
        mul = str2num(num1)*str2num(num2)
        if mul == 0:
            return "0"
        ret = ""
        while mul > 0:
            ret = str(mul%10) + ret
            mul /=10
        return ret


        
# @lc code=end

