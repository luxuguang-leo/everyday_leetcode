#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #method, 2 pointers， O(m+n)
        '''
        i = j = 0
        while  j < len(t):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i +=1
            j +=1
        return i == len(s)
        '''
        #DP,画出DP表，通项公式应该是:
        #s[i-1] == t[j-1]:DP[i][j] = DP[i-1][j-1]  
        #s[i-1] != t[j-1]:DP[i][j] = DP[i][j-1]
        #晕菜 竟然TLE。。。O(m*n)
        '''
        m, n = len(s), len(t)
        DP = [[False]*(n+1) for _ in range(m+1)]
        for j in range(n+1):
            DP[0][j] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = DP[i][j-1]
        return DP[-1][-1]
        '''
        #if not s:
            #return True
        #if not t:
            #return False
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1;j+=1
            else:
                j+=1
        return i == len(s)
        
# @lc code=end

