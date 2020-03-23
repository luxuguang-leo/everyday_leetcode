#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def dfs(self, board, x, y, pos, word):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if board[x][y] != word[pos]:
            return False
        if pos == len(word) -1:
            return True
        tmp = board[x][y]
        board[x][y] = '#'
        #if one direction satify DFS condation, continue DFS till end
        ret = self.dfs(board, x+1, y, pos+1, word) or self.dfs(board, x, y+1, pos+1, word) or \
              self.dfs(board, x-1, y, pos+1, word) or self.dfs(board, x, y-1, pos+1, word)
        board[x][y] = tmp
        return ret
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, 0, word):
                    return True
        return False
        
        
# @lc code=end

