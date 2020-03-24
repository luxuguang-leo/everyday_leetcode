#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode(object):
    def __init__(self):
        self.isleaf = False
        self.children = {}
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        parent = self.root
        for ch in word:
            if ch not in parent.children:
                parent.children[ch] = TrieNode()
            parent = parent.children[ch]
        parent.isleaf = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        parent = self.root
        for ch in word:
            if ch not in parent.children:
                return False
            else:
                parent = parent.children[ch]
        return parent.isleaf
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return False
        parent = self.root
        for ch in prefix:
            if ch in parent.children:
                parent = parent.children[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

