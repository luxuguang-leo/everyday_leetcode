#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        '''
        if not obstacleGrid:
            return 
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] * (1 - obstacleGrid[0][j])
        for i in range(1, m):
            for j in xrange(1, n):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]
        '''
        #clear code
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        DP = [[0]*n for _ in range(m)]
        DP[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                DP[i][0] = DP[i-1][0]
            else:
                DP[i][0] = 0
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                DP[0][j] = DP[0][j-1]
            else:
                DP[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = 0
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[-1][-1]
