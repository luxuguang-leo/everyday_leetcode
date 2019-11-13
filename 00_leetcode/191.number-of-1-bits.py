#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        cnt = 0
        while n> 0:
            cnt += (n & 0x01) 
            #cnt += (n %2) 
            n = n>>1
        return cnt
        '''
        #每一次和-1与，消除一个1
        cnt = 0
        while n>0:
            n = n&(n-1)
            cnt +=1
        return cnt

        


# @lc code=end

