#
# @lc app=leetcode id=201 lang=python
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #观察规律，应该是m,n左边共同部分，m,n同时右移，如果相同停止，将结果左移之前次数
        cnt = 0
        while m != n:
            m = m >>1
            n = n >>1 
            cnt +=1
        return (m<<cnt)
        #第二种方式
        '''
        while m<n:
            n &= (n-1)
        return n
        '''
        # @lc code=end

