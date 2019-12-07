#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #双指针,注意不需要用map,因为子序列有顺序要求，用map无法对应顺序
        i = j = 0
        while j < len(t):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
            j +=1
        return i == len(s)
        
# @lc code=end

