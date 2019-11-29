#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        #将(x,y)和(0,0)形成的最大正方形面积转化为(x-1, y-1)和(0,0)形成的正方形区域之间的关系
        #DP[x][y]表示(x,y)与(0,0)形成的区域的最大正方形面积
        #DP[x][y] = DP[x-1][y] + DP[x][y-1] - DP[x-1][y-1] + matrix[x][y]
        '''
        r, c = len(matrix), len(matrix[0])
        DP = [[0]*c for _ in range(r)]
        max_area = DP[0][0] = ord(matrix[0][0])-ord('0')
        for i in range(1,r):
            DP[i][0] = DP[i-1][0] +ord(matrix[i][0]-ord('0'))
        for i in range(1, c):
            DP[0][i] = DP[0][i-1] + ord(matrix[0][i])-ord('0')
        for i in range(1, r):
            for j in range(1,c):
                DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + ord(matrix[i][j])-ord('0')
                max_area = max(max_area, DP[i][j])
        return max_area
        '''
        #DP表示(x,y)和(0, 0)形成的区域最长的正方形边长
        #递推DP[x][y] = min(DP[x-1][y], DP[x][y-1], DP[x-1][y-1]) + matrix[x][y]
        r, c = len(matrix), len(matrix[0])
        DP = [[0]*c for _ in range(r)]
        max_len = 0
        for i in range(r):
            if matrix[i][0] == '1':
                DP[i][0] = 1
                max_len = 1
        for i in range(c):
            if matrix[0][i] == '1':
                DP[0][i] = 1
                max_len = 1
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == '1':
                    DP[i][j] = min(min(DP[i-1][j], DP[i][j-1]), DP[i-1][j-1]) + 1
                #else:
                    #DP[i][j] = min(min(DP[i-1][j], DP[i][j-1]), DP[i-1][j-1])
                max_len = max(max_len, DP[i][j])
        return max_len*max_len


# @lc code=end

