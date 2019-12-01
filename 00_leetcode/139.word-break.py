#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def helper(self, s, wordDict, hashmap):
        #寻找s时候可以被wordbreak,终止条件1.s就在wordDict 2.s在hashmap中，直接返回其结果
        if s in wordDict:
            hashmap[s] = True
            return True
        if s in hashmap:
            return hashmap[s]
        for i in range(1,len(s)):
            r = s[i:]
            #同样也可以将左右对调，也就是InDict("") && WB("leetcode")
            #if s[:i] in wordDict and self.helper(r, wordDict, hashmap):
            if r in wordDict and self.helper(s[:i], wordDict, hashmap):
                #hashmap[s[:i]] = True这里应该是整体都是True，而不是只处理左边
                hashmap[s] = True
                return True
        #如果都不满足则标记为False
        hashmap[s] = False
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return False
        #1.递归，
        # a.比如leetcode
        # WB("") && InDict("leetcode") ||
        # WB("l") && InDict("eetcode") ||
        # WB("le") && InDict("etcode") ||
        # WB("lee") && InDict("tcode") ||
        # WB("leet") && InDict("code")
        #...
        #b.如果InDict为True才会继续递归左半部分,也就是遇到InDict("code")
        #WB("leet"),这时候如果记忆化左半部分会直接得出结论，否则还要递归
        '''
        wordDict = set(wordDict)
        return self.helper(s, wordDict, {})
        '''
        #DP， DP[i]表示s[0..i-1]是否可以被分割
        #DP[i] = DP[0]&&InDict(s[0..i-1]) ||
        #DP[1]&&InDict(s[1...i-1]) ||
        #DP[2]&&InDict(s[2...i-1])
        #...
        #DP[i-1]&&InDict[i-1...i-1]
        DP = [False]*(len(s)+1)
        DP[0] = True
        for i in range(len(s)):
            if DP[i]:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict:
                        DP[j+1] = True
        return DP[-1]

        


            
        
# @lc code=end

