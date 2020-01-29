#
# @lc app=leetcode id=336 lang=python
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        '''
        l, r = 0, len(s)-1
        while l < r: 
            if s[l] == s[r]:
                l +=1; r -=1
            else:
                return False
        return True
        '''
        return s == s[::-1]
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        '''
        #TLE
        ret = []
        for i in range(len(words)):
            for j in range(len(words)):
                if j == i:
                    continue
                tmpStr = words[i]+words[j]
                if self.isPalindrome(tmpStr):
                    ret.append([i, j])
        return ret
        '''
        #基本判断方法，使用hashmap，存起来单词和索引
        #对于单词可以分为前缀和后缀，如果前缀是回文，那么如果后缀的倒叙在字典中就可以匹配成
        '''
        word_map = {w:i for i,w in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pre, pos = word[:j], word[j:]
                if pre==pre[::-1] and pos[::-1] != word \
                    and pos[::-1] in word_map:
                        res.append([word_map[pos[::-1]], i])
                if j != len(word) and pos==pos[::-1] \
                    and pre[::-1] != word and pre[::-1] in word_map:
                        res.append([i, word_map[pre[::-1]]])
        return res
        '''
        word_map = {}
        ret, selfPalidrome = [], []
        for idx, w in enumerate(words):
            word_map[w] = idx
            #对于自身是回文的情况
            if w == w[::-1]:
                selfPalidrome.append(idx)
        for i, word in enumerate(words):
            if word:
                #注意是len(word),这里面已经剔除了重复元素，包含了自身单词的回文的情况
                for j in range(len(word)):
                    pre, pos = word[:j], word[j:]
                    #print("split word", i, pre, pos)
                    if pre == pre[::-1] and pos[::-1] in word_map and i != word_map[pos[::-1]]:
                        ret.append([word_map[pos[::-1]], i])
                    if pos == pos[::-1] and pre[::-1] in word_map and i != word_map[pre[::-1]]:
                        ret.append([i, word_map[pre[::-1]]])
            #对于空字符的情况
            else:
                for loc in selfPalidrome:
                    if loc != i:
                        ret.append([i, loc])
        return ret

        



        
        
# @lc code=end

