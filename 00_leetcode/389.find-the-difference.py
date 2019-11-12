#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        if not s:
            if len(t) == 1:
                return t
            else:
                return ""
        hashmap = {}
        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 1
            else:
                hashmap[ch] +=1
        for ch in t:
            if ch not in hashmap or hashmap[ch] == 0:
                return ch
            else:
                hashmap[ch] -=1
        return ''
        '''
        sc = collections.Counter(s)
        tc = collections.Counter(t)
        for ch in tc:
            if sc[ch] != tc[ch]:
                return ch
                
        
# @lc code=end

