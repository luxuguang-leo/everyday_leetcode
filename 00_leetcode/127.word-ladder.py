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
        #BFS,可以按照每次找只有一个不同的字母的单次，进行BFS，然后标记为已经已经访问，知道第一次找到endWord 每一层有点类似brutal force,然后遍历
        queue = collections.deque([(beginWord, 1)])
        chars = string.ascii_lowercase
        wordSet = set(wordList)
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in xrange(len(word)):
                for j in chars:
                    if j != word[i]:
                        newWord = word[:i]+j+word[i+1:]
                        if newWord not in visited and newWord in wordSet:
                            queue.append((newWord, dist+1))
                            visited.add(newWord)  # wordList.remove(newWord)
                            wordSet.remove(newWord)
        return 0
        
# @lc code=end

