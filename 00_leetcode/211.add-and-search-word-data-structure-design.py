#
# @lc app=leetcode id=211 lang=python
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start

class TrieNode(object):
    def __init__(self):
        self.end = False
        self.children = dict()

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.children: #不存在
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        

    def __search(self, word, cur):
        if not word:
            return cur.end
        w = word[0]
        if w != '.':
            if w in cur.children:
                return self.__search(word[1:], cur.children[w])
            else:
                return False
        else:#如果是'.'，表示通配符，应该在所有的子节点中继续递归
            for child in cur.children.values():
                if self.__search(word[1:], child):
                    return True
        return False

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__search(word, self.root)
       

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

