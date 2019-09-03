#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashtable = {}
        for ch in magazine:
            if ch not in hashtable:
                hashtable[ch] = 1
            else:
                hashtable[ch] += 1
        for ch in ransomNote:
            if ch in hashtable:
                hashtable[ch] -= 1
                if hashtable[ch] < 0:
                    return False
            else:
                return False
        return True
        

