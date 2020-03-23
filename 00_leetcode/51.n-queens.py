#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#

# @lc code=start
class Solution(object):
    def isSafe(self, board, k, n):
        #判断第k个皇后可不可以放在第n列
        for i in range(k):
            if board[i] == n or abs(k-i) == abs(n-board[i]):
                return False
        return True


    def dfs(self, level, board, path, res):
        if level == len(board):
            res.append(path)
            return res
        for i in range(len(board)):
            if self.isSafe(board, level, i):
                board[level] = i
                s = '.'*len(board)
                #append each row in the path list
                self.dfs(level+1, board, path+[s[:i]+'Q'+s[i+1:]], res)


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        #board用一纬数组表示，按顺序表示第n个皇后应该放的列数
        board = [-1 for i in range(n)]
        res = []
        self.dfs(0, board, [],res)
        return res
        
# @lc code=end

