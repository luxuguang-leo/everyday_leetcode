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
        hash_set = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        #key point if hash_set[i] < hash_set[i+1], we can temporarily set -hast_set[i]
        ret = 0
        for i in range(len(s)-1):
            if hash_set[s[i]] < hash_set[s[i+1]]:
                ret -= hash_set[s[i]]
            else:
                ret += hash_set[s[i]]
        ret += hash_set[s[-1]]
        return ret
        

