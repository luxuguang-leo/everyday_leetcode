#
# @lc app=leetcode id=97 lang=python
#
# [97] Interleaving String
#

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #好难啊，二维DP
        #定义 DP[i][j]，表示长度为i+j的s3可以由长度为i的s1, 长度为j的s2交织构成
        #初始 DP[0][0] 为True
        #状态转移方程
        #DP[i][j] = DP[i-1][j] if s1[i-1] = s3[i+j-1]
        #DP[i][j] = DP[i][j-1] if s2[j-1] = s3[i+j-1]
        #结果DP[-1][-1]
        if len(s1) + len(s2) != len(s3):
            return False
        M, N = len(s1), len(s2)
        DP = [[False]*(N+1) for _ in range(M+1)]
        #DP[0][0] = True
        #if s3[]
        for i in range(M+1):
            for j in range(N+1):
                if i == 0 and j == 0:
                    DP[i][j] = True
                elif i > 0 and DP[i-1][j] and s3[i+j-1] == s1[i-1]:
                    DP[i][j] = True
                elif j > 0 and DP[i][j-1] and s3[i+j-1] == s2[j-1]:
                    DP[i][j] = True
                else:
                    DP[i][j] = False
        return DP[M][N]
        
        
# @lc code=end

