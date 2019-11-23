#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode(object):
    def __init__(self):
        self.end = False
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
        if not word:
            return 
        cur = self.root
        for w in word:#可以合并，但是为了方便理解不合并
            if w in cur.children:
                cur = cur.children[w]
            else:
                cur.children[w] = TrieNode()
                cur = cur.children[w]
        cur.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        cur = self.root
        for w in word:
            if w not in cur.children:
                return False
            else:
                cur = cur.children[w]
        #看最后一个节点的标识是否能行程word，true
        return cur.end


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        #prefix条件是最终子节点的时候不需要判断是否end,因为如果只是单次的一部分就不end
        if not prefix:
            return False
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

