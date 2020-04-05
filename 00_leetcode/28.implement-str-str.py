#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        i = 0
        m, n = len(haystack), len(needle)
        while i < m-n+1:
            j = 0
            while j < n and haystack[i+j] == needle[j]:
                j+=1
            if j == n:
                return i
            i+=1
        return -1

        #method 1
        '''
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            if needle == haystack[i:i+n]:
                return i
        return -1
        '''
        #method 2
        '''
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            j = 0
            while j < n and haystack[i+j] == needle[j]:
                j+=1
            if j == n:
                return i
        return -1
        '''

        
# @lc code=end

