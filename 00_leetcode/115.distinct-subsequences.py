#
# @lc app=leetcode id=115 lang=python
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #DP, DP table
        '''
          Ø r a b b b i t
        Ø 1 1 1 1 1 1 1 1
        r 0 1 1 1 1 1 1 1
        a 0 0 1 1 1 1 1 1
        b 0 0 0 1 2 3 3 3
        b 0 0 0 0 1 3 3 3
        i 0 0 0 0 0 0 3 3
        t 0 0 0 0 0 0 0 3
        '''
        #例子：S= "rabbbit", T = "rabbit", DP[len(T)+1][len(S)+1]
        #DP[i][j]表示S[0...j-1]的子串中能组成T[0...i-1]的个数
        #i == 0, DP[0][j] ==1，表示S包含空字符的个数
        #j == 0, DP[i][j] ==0 i > 0,表示空字符转换成T的个数，不可能所以为0
        #a. DP[i][j] = DP[i][j-1] if S[j-1] != T[i-1],表示如果S[j-1]和T[i-1]这位置字符不相等，
        ## 那么至少保证S[i-1]这个字符没有添加前的状态个数
        #b. DP[i][j] = DP[i][j-1] + DP[i-1][j-1]， 如果S[j-1]和T[i-1]相等，有两个选择
        # 要么用之前的匹配DP[i][j-1],要么这个S新增加的字符和T新增加的字符作为匹配的一部分，DP[i-1][j-1]
        '''
        M, N = len(s), len(t)
        DP = [[0]*(M+1) for _ in range(N+1)]
        for j in range(M+1):
            DP[0][j] = 1
        for i in range(1,N+1):
            for j in range(1, M+1):
                if s[j-1] != t[i-1]:
                    DP[i][j] = DP[i][j-1]
                else:
                    DP[i][j] = DP[i][j-1] + DP[i-1][j-1]
        return DP[-1][-1]
        '''
        #@0310，之前的解释有误，重新绘制DP表,选取纵坐标为S,横坐标为T
        '''
          Ø r a b b i t
        Ø 1 0 0 0 0 0 0
        r 1 1 0 0 0 0 0
        a 1 1 1 0 0 0 0
        b 1 1 1 1 0 0 0
        b 1 1 1 2 1 0 0
        b 1 1 1 3 3 0 0
        i 1 1 1 3 3 3 0
        t 1 1 1 3 3 3 3
        '''
        M, N = len(s), len(t)
        DP = [[0]*(N+1) for _ in range(M+1)]
        for i in range(M+1):
            DP[i][0] = 1
        for i in range(1, M+1):
            for j in range(1, N+1):
                if s[i-1] != t[j-1]:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
        return DP[M][N]

        
# @lc code=end

