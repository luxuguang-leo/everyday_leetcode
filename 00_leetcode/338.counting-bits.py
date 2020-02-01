#
# @lc app=leetcode id=338 lang=python
#
# [338] Counting Bits
#

# @lc code=start
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        '''
        ret = []
        for i in range(num+1):
            l = 0
            while i != 0:
                if i&1 == 1:
                    l +=1
                i = i>>1
            ret.append(l)
        return ret
        '''
        #method 2,对于偶数而言，i 和i/2的1的个数一致
        #对于奇数而言是i/2+1
        ret = [0]*(num+1)
        for i in range(1,num+1):
            if i %2 == 0:
                ret[i] = ret[i/2]
            else:
                ret[i] = ret[i/2]+1
        return ret
        
# @lc code=end

