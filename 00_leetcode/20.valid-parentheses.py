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
        #使用map完成左右括弧的映射
        if not s:
            return True
        m = {'}':'{', ']':'[', ')':'(' }
        q = []
        for ch in s:
            if ch not in m:
                q.append(ch)
            elif not q or q.pop() != m[ch]:
                return False
        return len(q) == 0


