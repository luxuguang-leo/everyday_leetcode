#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        if not haystack and not needle: 
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
        '''
        if needle == "":
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            j = 0
            while j < n and needle[j] == haystack[i+j]:
                j +=1
            if j == n:
                return i
        return -1

        

