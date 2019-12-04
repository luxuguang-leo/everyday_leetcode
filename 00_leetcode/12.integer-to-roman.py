#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
            [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
            [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]
        ]
        index = 0
        ret = ""
        while num > 0:
            if num >= m[index][0]:
                ret += m[index][1]
                num -= m[index][0]
            else:
                index +=1
        return ret

# @lc code=end

