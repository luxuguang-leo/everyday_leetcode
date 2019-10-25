#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidColumn(self, board):
        n = len(board)
        for r in range(n):
            row = [x for x in board[r] if x != '.']
            if len(set(row)) != len(row):
                return False
        return True

    def isValidRow(self, board):
        n = len(board)
        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(set(col)) != len(col):
                return False
        return True
         
    def isValidGrid(self, board):
        n = len(board)
        for r in range(0, n , 3):
            for c in range(0, n, 3):
                grid = []
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] != '.':
                            grid.append(board[r + i][c + j])
                if len(set(grid)) != len(grid):
                    return False
        return True


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidColumn(board) and self.isValidRow(board) and self.isValidGrid(board)
        
# @lc code=end

