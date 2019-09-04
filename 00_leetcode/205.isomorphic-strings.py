#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashS, hashT = {}, {}
        for i in range(len(s)):
            if s[i] not in hashS:
                hashS[s[i]] = i +1
            if t[i] not in hashT:
                hashT[t[i]] = i +1
            if hashS[s[i]] != hashT[t[i]]:
                return False
        return True
        

