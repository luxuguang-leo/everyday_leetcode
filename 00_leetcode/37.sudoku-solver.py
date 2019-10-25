#
# @lc app=leetcode id=37 lang=python
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution(object):
    #'''
    def isValid(self, board, r, c):
        tmp = board[r][c]
        board[r][c] = '.'
        for i in range(9):
            if board[r][i] == tmp:
                return False
            if board[i][c] == tmp:
                return False
            if board[r-r%3+i/3][c-c%3+i%3]== tmp:
            #if board[r/3*3+i/3][c/3*3+i%3]== tmp:
                return False
        board[r][c] = tmp
        return True
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    #for ch in [str(n) for n in range(1,10)]:
                    for ch in '123456789':
                        board[r][c] = ch
                        if self.isValid(board, r, c) and self.solveSudoku(board):
                            return True
                        board[r][c] = '.'
                    return False
        return True
# @lc code=end

