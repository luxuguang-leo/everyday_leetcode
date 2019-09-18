#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#
class Solution(object):
    def helper(self, n, tmp):
        tmp[1], tmp[2] = 1,2
        if n > 0 and tmp[n] == 0:
            tmp[n] = self.helper(n-1, tmp) + self.helper(n-2, tmp)
        return tmp[n]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #1. recursive,TLE
        '''
        if n <=2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
        #2. DP, top-down
        '''
        if n <=2:
            return n
        tmp = [0]*(n+1)
        self.helper(n, tmp)
        return tmp[n]
        '''
        #3. DP, bottom-up
        '''
        if n <=2:
            return n
        tmp = [0]*(n+1)
        tmp[0] = 0
        tmp[1] = 1
        tmp[2] = 2
        for i in range(3, n+1):
            tmp[i] = tmp[i-1] + tmp[i-2]
        return tmp[n]
        '''
        #4. DP, bottom-up, no memory array
        if n <= 2:
            return n
        prepre, pre = 1, 2
        for _ in range(3, n+1):
            sum = prepre + pre
            pre,  prepre= sum, pre
        return sum

        

