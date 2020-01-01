#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#

# @lc code=start
class Solution(object):
    def liveOrDeath(self, board, i, j):
        #judge (i, j) live or dead
        directions = [[1,1], [1,-1], [1,0], [-1, 1], [-1, -1], [-1, 0], [0, 1], [0,-1]]
        live_cnt = 0
        row, col = len(board), len(board[0])
        for point in directions:
            r, c = point[0] + i, point[1] +j
            if 0 <= r < row and 0 <= c < col:
                if board[r][c] == 1:
                    live_cnt +=1
        if live_cnt < 2 or live_cnt > 3:
            return 2
        elif board[i][j] == 1 or (board[i][j] == 0 and live_cnt >=3):
            return 1
        return 0
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #use deep copy, and brutal force?
        if not board:
            return []
        board_copy = copy.deepcopy(board)
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                ret = self.liveOrDeath(board, i, j)
                if ret == 2:#dead
                    board_copy[i][j] = 0
                elif ret == 1:#live
                    board_copy[i][j] = 1
        for i in range(row):
            for j in range(col):
                board[i][j] = board_copy[i][j]
        return board
        
        
        
# @lc code=end

