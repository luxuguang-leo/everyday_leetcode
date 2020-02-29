#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #@0229
        #method 1,如果可以被2整除，一直整除，直到为1
        '''
        if n <= 0:
            return False
        while n&0x01 == 0:
            n //= 2
        return n ==1
        '''
        #method 2,recrusatively
        '''
        if n <= 0:
            return False
        if n == 1:
            return True
        return (n&0x01==0 and self.isPowerOfTwo(n//2))
        '''
        #method 3,如果是2的幂次方，满足n&(n-1) == 0条件，因为只有一个1
        if n <= 0:
            return False
        return n&(n-1) == 0
        #直接数1的二级制个数，为1
        
# @lc code=end

