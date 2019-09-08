#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for ch in s:
            ret = ret * 26 + ord(ch) - ord('A') + 1
        return ret
        

