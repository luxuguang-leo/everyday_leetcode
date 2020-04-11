#
# @lc app=leetcode id=329 lang=python
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        #BFS, topological sort
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        q = collections.deque()
        degree = {}
        directions = [[0,1], [1,0], [0, -1], [-1, 0]]
        for i in range(M):
            for j in range(N):
                cnt = 0
                for dire in directions:
                    x, y = i + dire[0], j + dire[1]
                    if 0 <= x < M and 0<= y < N and matrix[x][y] < matrix[i][j]:
                        cnt+=1
                #momory each node's indegree
                degree[(i, j)] = cnt
                if cnt == 0:
                    q.append((i, j))
                
        step = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dire in directions:
                    nx, ny = x + dire[0], y + dire[1]
                    if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] > matrix[x][y] and (nx, ny) in degree:
                        degree[(nx,ny)] -=1
                        if degree[(nx, ny)] == 0:
                            q.append((nx, ny))
            step +=1
        return step
        
# @lc code=end

