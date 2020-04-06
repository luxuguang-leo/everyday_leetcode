#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
            return 0
        #直接标记为0防止重复访问，但是会改变原有的值
        grid[x][y] = '0'
        self.dfs(grid, x+1, y)
        self.dfs(grid, x, y+1)
        self.dfs(grid, x-1, y)
        self.dfs(grid, x, y-1)
        return 1


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #DFS，回溯，对于一个'1'的点DFS四个方向的值，如果是'0'就标记为island,
        #需要标记是否访问过？
        '''
        if not grid:
            return 0
        cnt = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    #DFS其四个方向
                    cnt += self.dfs(grid, i, j)
        return cnt
        '''
        #BFS, use queue,但是会修改原有矩阵
        if not grid:
            return 0
        cnt = 0
        q = collections.deque([])
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    cnt +=1
                    grid[i][j] = '0'
                    q.append([i, j])
                    while q:
                        x, y = q.popleft()
                        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                        for d in directions:
                            new_x, new_y = x + d[0], y + d[1]
                            if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                q.append([new_x, new_y])
        return cnt


        

        
# @lc code=end

