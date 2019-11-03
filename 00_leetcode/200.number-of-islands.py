#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def dfs(self, grid, m, n):
        if m < 0 or m >= len(grid) or n < 0 or n >= len(grid[0]) or grid[m][n] == "0":
            return 0
        grid[m][n] = "0"
        self.dfs(grid, m+1, n); self.dfs(grid, m-1, n)
        self.dfs(grid, m, n+1); self.dfs(grid, m, n-1)
        return 1
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #DFS
        #'''
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ret_nums = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ret_nums += self.dfs(grid, i, j)
        return ret_nums
        #'''

        #BFS,大概思路就是遇到"1"就加上去，置为"0"，然后压队列，弹队列，相邻是"1"继续压队，直到队列为空
        '''
        if not grid:
            return 0
        dq = collections.deque([])
        m, n = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        ret_nums = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ret_nums +=1
                    grid[i][j] = "0"
                    dq.append([i, j])
                    while dq:
                        r, c = dq.popleft()
                        for d in directions:
                            new_r, new_c = r + d[0], c + d[1]
                            if new_r >=0 and new_r < m and new_c >= 0 and new_c < n and grid[new_r][new_c] == "1":
                                grid[new_r][new_c] = "0"
                                dq.append([new_r, new_c])
        return ret_nums 
        '''

        
# @lc code=end

