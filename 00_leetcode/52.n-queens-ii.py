#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#

# @lc code=start
class Solution(object):
    def isSafe(self, r, c, board):
        for i in range(r):
            #there are 2 cases:in the same columu or in the diagonal line
            if board[i] == c or abs(r-i) == abs(board[i] - c):
               return False
        return True

    def dfs(self, depth, board):
        if depth == len(board):
           self.cnt +=1
           return self.cnt
        for i in range(len(board)):
            if self.isSafe(depth, i, board):
                board[depth] = i
                self.dfs(depth+1, board)


   
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = 0
        board = [-1 for i in range(n)]
        self.dfs(0, board)
        return self.cnt







        
# @lc code=end

