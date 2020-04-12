#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#
class Solution(object):
    def dfs(self, s, path, ret):
        if len(s) == 0:
            ret.append(path)
            return ret
        #the right boundary is len(s)+1, if not, we ignore the last character in s
        for i in range(1, len(s)+1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
            #if self.isPalindrome(prefix):
                self.dfs(s[i:], path+[prefix], ret)
        

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        ret = []
        self.dfs(s, [], ret)
        return ret
        

