#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split()
        if not pattern or not str or len(pattern) != len(s):
            return False
        chDict = {}
        wordDict = {}
        for i in range(len(pattern)):
            if pattern[i] not in chDict:
                chDict[pattern[i]]= i
            if s[i] not in wordDict:
                wordDict[s[i]] = i
            if chDict[pattern[i]] != wordDict[s[i]]:
                return False
        return True
 
        

