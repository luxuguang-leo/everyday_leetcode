#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        #DP = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    DP[i][j] = 1
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
        #return DP[m-1][n-1]
        return DP[-1][-1]
        '''
        #简单的二维DP，注意处理边界即可
        DP = [[0]*n for _ in range(m)]
        for i in range(m):
            DP[i][0] = 1
        for j in range(n):
            DP[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i][j-1] + DP[i-1][j]
        return DP[-1][-1]
        

