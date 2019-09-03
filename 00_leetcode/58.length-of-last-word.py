#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                if cnt == 0:
                    continue
                else:
                    break
            else:
                cnt +=1
        return cnt

        

