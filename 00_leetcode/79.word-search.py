#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    #记录走过的点
    def dfs(self, x, y, board, start, word):
        if x == len(board) or y == len(board[0]) or x < 0 or y < 0 or word[start] != board[x][y]:
            return False
        if start == len(word)-1:
            return True
        char = board[x][y]
        board[x][y] = 0
        ret = self.dfs(x+1, y, board, start+1, word) or self.dfs(x, y+1, board, start+1, word) or self.dfs(x-1, y, board, start+1, word) or self.dfs(x, y-1, board, start+1, word)
        board[x][y] = char
        return ret

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #题目理解，找出是否包含此字母每一个字符，并且这个区域是相邻的
        #DFS解这类问题比较适合，我的纠结点在于如何标记已经走过的点
        if not word or not board:
            return False
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if self.dfs(i, j, board, 0, word):
                    return True
        return False
        
# @lc code=end

