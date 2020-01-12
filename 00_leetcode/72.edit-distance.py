#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #一般二维DP，设计到两个字符串，求最值问题
        #字符串类动态规划， DP[m][n]表示从str1(0..m)转换到str(0..n)的代价
        #依照最后一个字符是否相等得到递推公式
        #if s[m] == s[n] DP[m][n] = DP[m-1][n-1]
        #if s[m] != s[n] DP[m][n] = min(DP[m-1][n], DP[m][n-1], DP[m-1][n-1]) +1
        M, N = len(word1), len(word2)
        DP = [[0]*(N+1) for _ in range(M+1)]
        #需要考虑特殊情况，当其中一个字符为空的时候返回的另一个字符长度
        for i in range(M+1):
            DP[i][0] = i
        for i in range(N+1):
            DP[0][i] = i
        for i in range(1,M+1):
            for j in range(1,N+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(min(DP[i-1][j], DP[i][j-1]), DP[i-1][j-1])+1
        return DP[M][N]

        
        
# @lc code=end

