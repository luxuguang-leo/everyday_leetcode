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
        #brutal force, 判断是p的异构词语，排序,但是会TLE
        '''
        p = sorted(p)
        w = len(p)
        ret = []
        for i in range(len(s)-w+1):
            sub_str = sorted(s[i:i+w])
            if sub_str == p:
                ret.append(i)
        return ret
        '''
        #method 2，用map表来比较两个字符,这时候左边界是l-w+1
        m = collections.Counter(p)
        h = collections.Counter()
        ret = []
        w = len(p)
        for i in range(len(s)):
            h[s[i]] +=1
            if i >= w:
                h[s[i-w]] -=1
                if h[s[i-w]] == 0:
                    del h[s[i-w]]
            if h == m:
                ret.append(i-w+1)
        return ret


            

        
# @lc code=end

