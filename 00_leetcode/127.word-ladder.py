#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #BFS,可以按照每次找只有一个不同的字母的单次，进行BFS，
        #然后标记为已经已经访问，知道第一次找到endWord, 用 queue完成bfs
        if not beginWord or not endWord or not wordList:
            return 0
        q = collections.deque([(beginWord, 1)])
        chars = string.ascii_lowercase
        wordset = set(wordList)
        visited = set()
        visited.add(beginWord)
        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            for i in range(len(word)):
                for j in chars:
                    if j != word[i]:
                        new_word = word[:i] + j + word[i+1:]
                        if new_word in wordset and new_word not in visited:
                            visited.add(new_word)
                            q.append([new_word, depth+1])
                            wordset.remove(new_word)
        return 0

            
       
        
# @lc code=end

