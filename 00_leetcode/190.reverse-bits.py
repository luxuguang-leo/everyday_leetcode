#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n>>i)&0x01
        return reversed

# @lc code=end

