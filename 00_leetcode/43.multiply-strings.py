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
        #return str(int(num1)*int(num2))
        def str2num(str):
            ret = 0
            for ch in str:
                val = ord(ch) - ord('0')
                ret = ret*10 + val
            return ret
        mul = str2num(num1)*str2num(num2)
        ret = ""
        if mul == 0:
            return "0"
        while mul:
            ret = str(mul%10) + ret
            mul = mul/10
        return ret

        
# @lc code=end

