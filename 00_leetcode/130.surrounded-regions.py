#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def dfs(self, board, m, n):
        if m < 0 or m >= len(board) or n < 0 or n >= len(board[0]) or board[m][n] == "X":
            return
        if board[m][n] == "*":
            return 
        if board[m][n] == "O":
            board[m][n] = "*"
            self.dfs(board, m-1, n);self.dfs(board, m+1, n)
            self.dfs(board, m, n -1);self.dfs(board, m, n+1)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        ### BFS 使用队列
        '''
        dq = collections.deque([])
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == "O":
                    dq.append((i,j))
        while dq:
            r, c = dq.popleft()
            if 0 <= r < m and 0<=c < n and board[r][c] == "O":
                board[r][c] = "*"
                dq.append((r-1, c));dq.append((r, c-1))
                dq.append((r+1,c));dq.append((r, c+1))
        for i in range(m):
            for j in range(n):
                if board[i][j] == "*":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board
        '''
        #DFS,需要通过在边界找到的‘O’，继续DFS，找到‘O’边界标记为'*'
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if(i in [0, m-1] or j in [0, n-1]):
                    if board[i][j] == "O":
                        #board[i][j] = "*"#不应该在这里标记，否则DFS里的访问过判断会出问题
                        self.dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "*":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board



# @lc code=end

