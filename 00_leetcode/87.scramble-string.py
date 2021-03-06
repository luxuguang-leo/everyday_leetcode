#
# @lc app=leetcode id=87 lang=python
#
# [87] Scramble String
#

# @lc code=start
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #@0310
        if sorted(s1) != sorted(s2):
            return False
        if len(s1) < 4:#原因，小于四个字符长度，1，2，3的话都是可以乱序得到的
            return True
        #注意递归的终止条件
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
        
        
# @lc code=end

