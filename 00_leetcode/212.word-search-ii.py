#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#

# @lc code=start

class TrieNode(object):
    def __init__(self):
        self.end = False
        self.child = {}

class Solution(object):
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        if not word:
            return
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True

    def dfs2(self, x, y, board, Node, ret, path):
        if Node.end == True:
            ret.append(path)
            #mark it as already visited!!! Or you will found duplicate result
            Node.end = False
            #到此节点已经有单词？证明结果中的word已经搜索到了！！！所以将结果保存起来
            #别的解法里面有删除此word,但是有相同prefix的证明处理呢？
        #实现在矩阵中DFS，并且所走路径都存在于Trie
        #p.s.最后一个参数可以改成TrieNode，因为只有node里面含有当前字符，
        #才会进行下一个递归，当然下一个字符也在Trie的下一个节点中
        #用Trie则显得很复杂,另外不需要传递word单词了因为已经有了Trie参数
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return 
        c = board[x][y]
        if c not in Node.child:
            return 
        Node = Node.child[c]
        board[x][y] = '#'
        self.dfs2(x-1, y, board, Node, ret, path+c) 
        self.dfs2(x+1, y, board, Node, ret, path+c)
        self.dfs2(x, y-1, board, Node, ret, path+c)
        self.dfs2(x, y+1, board, Node, ret, path+c)
        board[x][y]= c
    
    def dfs(self, x, y, board, w, start):
        if x < 0 or x == len(board) or y < 0 or y == len(board[0]) or w[start] != board[x][y]:
            return False
        if start == len(w)-1:
            return True
        char = board[x][y]
        board[x][y] = 0
        result = self.dfs(x+1,y,board, w, start+1) or \
        self.dfs(x-1, y, board, w, start+1) or \
        self.dfs(x, y+1, board, w, start+1) or \
        self.dfs(x, y-1, board, w, start+1)
        board[x][y]= char
        return result

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #DFS,按照word search 算法只是增加一个for循环，但是会TLE！
        '''
        if not board or not words:
            return []
        ret = []
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                for word in words:
                    if self.dfs(i, j, board, word, 0):
                        #print(word)
                        ret.append(word)
        return set(ret)
        '''
        #Trie + DFS,因为如何建树，如何DFS，在哪里DFS
        #用Trie因为在大量单次有前缀，如果不用Trie，每一次都要重复搜索，DFS同样在矩阵中DFS，所走的路径必须在Trie中
        #所以需要首先根据words创建Trie树
        if not words or not board:
            return []
        for w in words:
            self.addWord(w)
        row, col = len(board), len(board[0])
        ret = []
        for i in range(row):
            for j in range(col):
                #for word in words,不需要遍历word的list,只需要遍历矩阵即可
                self.dfs2(i, j, board, self.root, ret, "")
        return ret

# @lc code=end

