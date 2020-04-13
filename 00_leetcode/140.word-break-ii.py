#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#

# @lc code=start
class Solution(object):
   def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        hashmap = {}
        wordSet = set(wordDict)
        def dfs(s):
            if s in hashmap:
                return hashmap[s]
            path = []
            if s in wordSet:
                path.append(s)
            for i in range(1, len(s)):
                r = s[i:]
                if r in wordSet:
                    path += [l +" "+ r for l in dfs(s[:i])]
            hashmap[s] = path
            return hashmap[s]
        return dfs(s)
        
# @lc code=end

