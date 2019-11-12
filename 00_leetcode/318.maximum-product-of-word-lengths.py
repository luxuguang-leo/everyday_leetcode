#
# @lc app=leetcode id=318 lang=python
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #bitmaps = collections.defaultdict(int)
        bitmaps = [0]*len(words)
        for i in range(len(words)):
            for c in words[i]:
                bitmaps[i] |= (1<<(ord(c)-ord('a')))
        max_len = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if bitmaps[i] & bitmaps[j] == 0:
                    max_len = max(max_len, len(words[i])*len(words[j]))
        return max_len

        
# @lc code=end

