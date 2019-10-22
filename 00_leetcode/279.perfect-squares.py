#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
class Solution(object):
    dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        #http://yucoding.blogspot.com/2016/12/leetcode-question-perfect-square.html
        #DP, little tricky, but simple
        #for one possible soluction, n = a + b*b
        #that's to say, DP[n] = DP[a] + 1
        '''
        DP = [0]*(n+1)
        DP[0], DP[1] = 0, 1
        for i in range(2, n+1):
            j = 0
            while j*j <= i:
                DP[i] = min(DP[i], DP[i - j*j] + 1)
        return DP[-1]
        '''
        dp = self.dp
        while len(dp) <= n:
            dp += [min(dp[-c*c] for c in range(1, int(len(dp)**0.5+1)))+1]
        return dp[n]

