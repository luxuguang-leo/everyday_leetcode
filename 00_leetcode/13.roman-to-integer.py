#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ret = 0
        for i in range(len(s)-1):
            if m[s[i]] < m[s[i+1]]:
                ret -= m[s[i]]
            else:
                ret += m[s[i]]
        return (ret + m[s[-1]])
