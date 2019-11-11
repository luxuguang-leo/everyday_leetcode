#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for i in [2,3,5]:
            while num % i == 0:
                num = num/i
        if num == 1:
            return True
        else:
            return False

        
# @lc code=end

