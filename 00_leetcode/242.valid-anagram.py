#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for ch in s:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch] +=1
        for ch in t:
            if ch in dict:
                dict[ch] -=1
            else:
                return False
        for val in dict.values():
            if val != 0:
                return False
        return True
        

