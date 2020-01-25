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
        #更新start的条件就是出现的字符串已经超过start,这时再以start为起点的字符串肯定包含重复字符，所以需要更新
        start, ans = 0, 0
        m = {}
        for i, ch in enumerate(s):
            if ch in m and start <= m[ch]:
                start = m[ch] + 1
            else:
                ans = max(ans, i - start + 1) 
            m[ch] = i
        return ans


        
# @lc code=end

