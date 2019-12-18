#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #分清出n的含义，分为个数1， 个数2， 个数3的情况
        #f(0) = 1
        #f(n) = f(0)*f(n-1) + ...+f(n-1)*f(0)
        #最终数目是相加
        '''
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]
        '''
        #refer to https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
        #G(N):represent the soluction
        #F(i, N):i as the root with all n numbers
        #G(N) = F(0, N)+F(1,N)+...+F(N,N)
        #F(i, N) = G(i-1)*G(N-i)  N>=i>=1 this is tricky,
        #G(N) = G(0)*G(N-1) + G(1)*G(N-2)+...+G(N-1)*G(0)
        DP = [0]*(n+1)
        DP[0] = 1
        for i in range(1, n+1):
            for j in range(0, i):
                DP[i] += DP[j]*DP[i-j-1]
        print(DP)
        return DP[-1]
        

