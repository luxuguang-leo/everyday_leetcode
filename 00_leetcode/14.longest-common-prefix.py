#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        l = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < l:
            if strs[0][i] == strs[-1][i]:
                i += 1
            else:
                break
        return strs[0][:i]
        

