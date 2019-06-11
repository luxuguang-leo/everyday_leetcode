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
        if not s:
            return 0
        left = max_len = 0
        map_list = {}
        for i in range(len(s)):
            if s[i] in map_list and left <= map_list[s[i]]:
                left = map_list[s[i]] + 1
            else:
                max_len = max(max_len, i - left+1)
            map_list[s[i]] = i
        return max_len
        

