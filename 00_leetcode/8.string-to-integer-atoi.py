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
        #corner case需要考虑
        #1.white space
        #2.正负符号记录
        #3.字符中间的非数字处理
        str = str.strip()
        if len(str) <= 0:
            return 0
        sign = 1
        if str[0] in '+-':
            if str[0] == '-':
                sign = -1
            str = str[1:]
        ret = 0
        for ch in str:
            if not ch.isdigit():
                break
            n = ord(ch) - ord('0')
            ret = ret*10 + n
        ret = sign* ret
        '''
        if ret > 2**31-1:
            return 2**31-1
        elif ret < -2**31:
            return -2**31
        else:
            return ret
        '''
        return min(2**31-1, max(-2**31, ret))
       
        
# @lc code=end

