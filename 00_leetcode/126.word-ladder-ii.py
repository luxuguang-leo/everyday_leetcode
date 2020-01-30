#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

# @lc code=start
class Solution(object):
    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        wordSet = set(wordList)
        wordSet.add(beginWord)
        wordSet.add(endWord)

        result = []
        cur = [beginWord]
        visited = set([endWord])
        found = False
        trace = {word: [] for word in wordList} 
        
        while cur and not found:
            for word in cur:
                visited.add(word)
                 
            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in wordSet:
                            if candidate == endWord:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next
             
        if found:
            self.backtrack(result, trace, [], endWord)
         
        return result
     
    
        
# @lc code=end

