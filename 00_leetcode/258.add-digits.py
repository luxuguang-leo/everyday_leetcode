#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        if num == 0:
            return 0
        return 1 + (num-1)%9
        '''
        while num >=10:
            num = num%10 + num/10
        return num
        
# @lc code=end

