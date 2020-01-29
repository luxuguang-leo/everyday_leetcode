#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #hashmap, stupid question
        hashTable = {}
        for ch in s:
            if ch not in hashTable:
                hashTable[ch] = 1
            else:
                hashTable[ch] += 1
        for i in range(len(s)):
            if hashTable[s[i]] == 1:
                return i
        return -1

        

