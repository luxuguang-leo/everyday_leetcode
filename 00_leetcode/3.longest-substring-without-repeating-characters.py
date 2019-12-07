#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #method 1， sliding window
        '''
        left = max_len = 0
        hTable = {}
        for i in range(len(s)):
            if s[i] in hTable and left <= hTable[s[i]]:
                left = hTable[s[i]] + 1
            else:
                max_len = max(max_len, i - left +1)
            hTable[s[i]] = i
        return max_len
        '''
        #method 2, sliding window,use pattern
        if len(s) <= 1:
            return len(s)
        l = max_len = 0
        m = {}
        for i in range(len(s)):
            m[s[i]] = m.get(s[i], 0) +1
            while m[s[i]] != 1:
                #左移窗口，更新map中的值
                m[s[l]] -=1
                l += 1
            max_len = max(max_len, i-l+1)
            #print(m, l, i, max_len)
        return max_len



        

