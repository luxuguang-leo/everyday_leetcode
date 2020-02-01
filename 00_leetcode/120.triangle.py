#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #method 1, DP, O[MxN]
        '''
        if not triangle:
            return
        DP = [[0 for i in xrange(len(row))] for row in triangle]
        DP[0][0] = triangle[0][0]
        for i in xrange(1,len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    DP[i][j] = DP[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) -1:
                    DP[i][j] = DP[i-1][j-1] + triangle[i][j]
                else:
                    DP[i][j] = min(DP[i-1][j], DP[i-1][j-1]) + triangle[i][j]
        return min(DP[-1])
        '''
        #method 2, DP, don't need to create, modify triangle in place
        '''
        if not triangle:
            return
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
        '''
        m = len(triangle)
        for i in range(1,m):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][0] += triangle[i-1][0]
                elif j == len(triangle[i])-1:
                    triangle[i][-1] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])
        

