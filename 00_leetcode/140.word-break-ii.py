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
        words = set(wordDict)
        mem = dict()
        def dfs(s):
            if s in mem:
                return mem[s]
            path = []
            if s in words:
                path.append(s)
            for i in range(1, len(s)):
                r = s[i:]
                if r not in words:
                    continue
                path +=[l + " "+ r for l in dfs(s[:i])]
                #print(path)
            mem[s] = path
            return mem[s]
        return dfs(s)

        
# @lc code=end

