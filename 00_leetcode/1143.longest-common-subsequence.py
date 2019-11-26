#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0
        M, N = len(text1), len(text2)
        DP = [[0]*(N+1) for i in range(M+1)]
        for i in range(1,M+1):
            for j in range(1, N+1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = DP[i-1][j-1]+1
                else:
                    DP[i][j] = max(DP[i][j-1], DP[i-1][j])
        return DP[M][N]
        
# @lc code=end

