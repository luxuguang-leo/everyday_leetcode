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
        '''
        #使用hashmap
        #出现左右拼接为回文有以下几种情况:
        #1.左为palindrome,右为空字符
        #2.左右倒叙，拼起来就是回文
        #3.左字符串左半部分为回文，右半部分和右字符串，{右字符串|左字符串回文部分|左字符串右字符串镜像}
        #4.左字符串右半部分为回文，左半部分与右字符串镜像，{左字符串右字符镜像|左字符回文|右字符串}
        #algo:将所有的字符和索引加入hashmap
        def isPalindrome(str):
            if not str:
                return True
            else:
                return str == str[::-1]
        hashmap = {}
        ret = set()
        for idx, w in enumerate(words):
            hashmap[w] = idx
        for idx, w in enumerate(words):
            #case 1
            if w and isPalindrome(w) and "" in hashmap:
                nidx = hashmap[""]
                ret.add((idx, nidx))
                ret.add((nidx, idx))
            #case 2
            reverseW = w[::-1]
            if w and reverseW in hashmap:
                nidx = hashmap[reverseW]
                if idx != nidx:
                    ret.add((idx, nidx))
                    ret.add((nidx, idx))
            #case 3 & 4
            for j in range(1, len(w)):
                leftstr, rightstr = w[:j], w[j:]
                if isPalindrome(leftstr) and rightstr[::-1] in hashmap:
                    ret.add((hashmap[rightstr[::-1]], idx))
                if isPalindrome(rightstr) and leftstr[::-1] in hashmap:
                    ret.add((idx, hashmap[leftstr[::-1]]))
        return list(ret)
                

        



        
        
# @lc code=end

