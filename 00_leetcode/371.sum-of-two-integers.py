#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #对低32位取模是因为对python希望在低32位进行操作，取模永远是正数
        MASK = 0xFFFFFFFF
        while b!=0:
            a, b = (a^b)&MASK, ((a&b)<<1)&MASK
        return a if a <= 0x7FFFFFFF else ~(a^MASK)
# @lc code=end

