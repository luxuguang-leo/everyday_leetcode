#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        '''
        if not s or not words:
            return []
        #sliding window方法，没有想到窗口大小，根据题意窗口大小应该是N*len(words[0])
        #然后按照这么大的固定窗口来滑动，匹配每一个len(word)大小的单词是否出现在map中
        #1.如果出现，将临时map更新，并比较和原始map是否小于等于，大于则不满足
        #2.如果不出现则继续滑动
        m = collections.Counter(words)
        w = len(words[0])
        #hash_s = {}
        window_size = w*len(words)
        if len(s) < window_size:
            return []
        ret = []
        for i in range(len(s)-window_size +1):
            hash_s = {}
            for j in range(0, window_size+1, w):#这里应该注意j的边界，并且根据j break时候的值判断有没有还整个window来匹配
                sub_str = s[i+j:i+j+w]
                #print("now",j, i, sub_str)
                if sub_str in m:
                    hash_s[sub_str] = hash_s.get(sub_str, 0) +1
                    #print(sub_str,hash_s[sub_str], i, j)
                    if hash_s[sub_str] > m[sub_str]:
                        break
                else:
                    break
            #print("loop once", j)
            if j == window_size:
                ret.append(i)
        return ret
        '''
        #@0309, sliding window
        # 使用两个map，一个记录所有word和次数 wordDict,另一个记录窗口内的出现的单次newDict
        #整个窗口的大小是所有单词组成的长度，在每一个窗口内，按照一个单词为单位匹配，有以下几种情况需要跳出将窗口右移动：
        #1.单词不在wordDict中 2.出现的单词次数大于wordDict  
        #2.如果整个窗口匹配，则记录窗口的起始位置
        #时间复杂度为O(m*n), m是整个字符串的长度，n为word的数目
        '''
        if not s or not words:
            return []
        #Counter is much slower than {} or dict
        #wordDict = collections.Counter(words)
        wordDict = collections.defaultdict(int)
        for w in words:
            wordDict[w] +=1
        wordLen = len(words[0])
        wordCount = len(words)
        windowLen = wordCount*wordLen
        strLen = len(s)
        ret = []
        for i in range(strLen - windowLen + 1):
            newWordDict = collections.defaultdict(int)
            for j in range(wordCount):
                subWord = s[i+j*wordLen: i+(j+1)*wordLen]
                if subWord in wordDict:
                    newWordDict[subWord] +=1
                    if newWordDict[subWord] > wordDict[subWord]:
                        break
                else:
                    break
            if newWordDict == wordDict:
                ret.append(i)
        return ret
        '''
        #method 2,判断重复的情况，如果窗口中单词发现已经超过了，可以直接将窗口的左边界右移动一个单词长度，
        #https://leetcode.wang/leetCode-30-Substring-with-Concatenation-of-All-Words.html
        #外循环是单词的长度，内循环是一个整个字符串减去单词长度的大的window，满足条件则右边界向右扩展，不满足条件则左边界向右扩展一个单词长度，
        #内外循环保证所有的情况都可以访问到，时间复杂度为O(m*len(word)),如果单词长度大大小于单词数目，则这一种方法比前一种时间复杂度提高,且有一些重复判断
        if not s or not words:
            return []
        lenWord = len(words[0])
        wanted = len(words)
        lenStr = len(s)
        ret = []
        if lenStr < lenWord*wanted:
            return ret
        wordDict = collections.defaultdict(int)
        for w in words:
            wordDict[w] +=1
        for i in range(lenWord):
            start, cnt = i, 0
            tmpWordDict = collections.defaultdict(int)
            for j in range(start, lenStr - lenWord +1, lenWord):
                subWord = s[j:j+lenWord]
                if subWord in wordDict:
                    tmpWordDict[subWord] +=1
                    cnt +=1
                    while tmpWordDict[subWord] > wordDict[subWord]:
                        tmpWordDict[s[start:start+lenWord]] -=1
                        start += lenWord
                        cnt -=1
                    if cnt == wanted:
                        ret.append(start)
                else:
                    #如果当前单词不在字典中，可以大大优化
                    #1.将tmphashmap清零
                    #2.将左边界从start直接拉到j+lenWOrd
                    #3.cnt清零
                    tmpWordDict = collections.defaultdict(int)
                    start = j+lenWord
                    cnt = 0
        return ret
        
        
# @lc code=end

