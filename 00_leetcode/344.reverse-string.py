#
# @lc app=leetcode id=344 lang=python
#
# [344] Reverse String
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        l = len(s)
        for i in range((l + 1)//2):
            s[i], s[l-1-i] = s[l-1-i], s[i]
        return s
        

