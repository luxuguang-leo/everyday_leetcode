#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #sliding window, record the position of each char
        '''
        start = 0
        ans = 0
        m = {}
        for i in range(len(s)):
            if s[i] in m and start <= m[s[i]]:
                start = m[s[i]] + 1
            else:
                ans = max(ans, i - start + 1) 
            m[s[i]] = i
        return ans
        '''
        start = 0
        ans = 0
        m = {}
        for i in range(len(s)):
            if s[i] in m and start <= m[s[i]]:
                start = m[s[i]] + 1
            ans = max(ans, i - start + 1) 
            m[s[i]] = i
        return ans


        
# @lc code=end

