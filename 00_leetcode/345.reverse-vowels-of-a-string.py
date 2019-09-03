#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l , r = 0, len(s)-1
        while l < r:
            while l < r and s[l].lower() not in vowels:
                l += 1
            while l < r and s[r].lower() not in vowels:
                r -= 1
            s[l], s[r] = s[r] , s[l]
            l += 1
            r -= 1
        return ''.join(s)

