#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        ret, cnt = '', 0
        for i in range(len(s)):
            cnt +=1
            if i == len(s)-1 or s[i] != s[i+1]:
                ret += str(cnt)
                ret += s[i]
                cnt = 0
        return ret
        

