#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        tmp_set = {'{':'}','[':']','(':')'}
        q = []
        for ch in s:
            if ch in tmp_set:
                q.append(tmp_set[ch])
            elif not q or q.pop() != ch:
                return False
        return len(q)==0

