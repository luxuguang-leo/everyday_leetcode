#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#

# @lc code=start
class Solution(object):
    def isSafe(self, board, k, j):
        for i in range(k):
            if board[i] == j or abs(k-i) == abs(board[i] - j):
                return False
        return True

    def dfs(self, level, board):
        if level == len(board):
            self.res_cnt +=1
            return self.res_cnt
        for i in range(len(board)):
            if self.isSafe(board, level, i):
                board[level] = i
                self.dfs(level+1, board)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res_cnt = 0
        board = [-1 for i in range(n)]
        self.dfs(0, board)
        return self.res_cnt







        
# @lc code=end

