#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def dfs(self, board, x, y, start, word):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[start]:
            return False
        if start == len(word) -1:
            return True
        tmp = board[x][y]
        board[x][y] = '#'#避免再次访问到
        ret = self.dfs(board, x+1, y, start + 1, word) or self.dfs(board, x, y+1, start + 1, word)\
            or self.dfs(board, x-1, y, start + 1, word) or self.dfs(board, x, y-1, start + 1, word)
        board[x][y] = tmp
        return ret
        

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #难点在于判断单个点和word的关系，对单独的一个点进行DFS的时候传入一个参数代表word的位置来解决此问题
        if not board or not word:
            return False
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if self.dfs(board, i, j, 0, word):
                    return True
        return False
        
        
# @lc code=end

