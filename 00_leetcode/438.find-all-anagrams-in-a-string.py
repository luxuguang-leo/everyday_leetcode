#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #和#76相同的思路！
        if not s or not p:
            return []
        m = collections.Counter(p)
        l, cnt = 0, 0
        wanted = len(p)
        ret = []
        for r in range(len(s)):
            if s[r] in m:
                m[s[r]] -=1
                if m[s[r]] >=0:
                    cnt +=1
            while cnt == wanted:
                if r - l + 1 == len(p):
                    ret.append(l)
                if s[l] in m:
                    m[s[l]] +=1
                    if m[s[l]] > 0:
                        cnt -=1
                l +=1
        return ret
        
# @lc code=end

