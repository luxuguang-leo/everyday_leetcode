#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return None
        row, col = len(grid), len(grid[0])
        DP = [[0]*col for _ in range(row)]
        #定义DP为从起始点到(x,y)的最小路径和，那么
        #递推公式 (x,y)点之能由(x-1, y)或者(x, y-1)获得
        #DP[x][y] = min(DP[x-1][y], DP[x][y-1]) + grid[x][y]
        #对边界特殊处理
        DP[0][0] = grid[0][0]
        for i in range(1, row):
            DP[i][0] = DP[i-1][0]+grid[i][0]
        for i in range(1, col):
            DP[0][i] = DP[0][i-1] + grid[0][i]
        for i in range(1, row):
            for j in range(1, col):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
        return DP[-1][-1]
        
# @lc code=end

