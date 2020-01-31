#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        def countPalind(s, l, r):
            cnt = 0
            while l >=0 and r < len(s):
                if s[l] == s[r]:
                    cnt +=1
                    l -=1; r +=1
                else:
                    break
            return cnt
        ret = 0
        for i in range(len(s)):
            ret += countPalind(s, i, i)
            ret += countPalind(s, i, i+1)
        return ret
# @lc code=end

