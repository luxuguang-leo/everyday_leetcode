#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #比较难想，如果出现三次，那么对于二进制来说1的个数肯定可以被3整除，最终消除3个数带来的1
        res = 0
        for i in range(32):
            sum_bits = 0
            for n in nums:
                sum_bits += ((n>>i)&01)
                #n = n>>1
            res |= (sum_bits%3)<<i
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res
# @lc code=end

