#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def dfs(self, board, m, n):
        if m < 0 or m >= len(board) or n < 0 or n >= len(board[0]) or \
            board[m][n] == 'X' or board[m][n] == '*':
            return
        #if board[m][n] == "O":
        board[m][n] = "*"
        self.dfs(board, m-1, n)
        self.dfs(board, m+1, n)
        self.dfs(board, m, n -1)
        self.dfs(board, m, n+1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #DFS
        '''
        if not board:
            return []
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if i == 0 or i == r-1 or j == 0 or j == c-1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)
        for i in range(r):
            for j in range(c):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'     
        return board  
        '''
        #BFS,相同思路，在边界寻找'O',BFS,然后标记为'*',思路通DFS
        if not board:
            return []
        r, c = len(board), len(board[0])
        q = collections.deque([])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(r):
            for j in range(c):
                if i == 0 or i == r-1 or j == 0 or j == c-1:
                    if board[i][j] == 'O':
                        board[i][j] = '*'
                        q.append([i, j])
                        while q:
                            x, y = q.popleft()
                            for d in directions:
                                x_new, y_new = x+d[0], y+d[1]
                                if 0 <= x_new < r and 0<= y_new < c:
                                    if board[x_new][y_new] == 'O':
                                        board[x_new][y_new] = '*'
                                        q.append([x_new, y_new])
        for i in range(r):
            for j in range(c):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board

                    
        



# @lc code=end

