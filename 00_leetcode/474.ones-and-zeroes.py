#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #二维DP类似， DP[i][j] = max(DP[i-zeros][j-ones]+1, DP[i][j])
        DP = [[0]*(n+1) for _ in range(m+1)]
        for str in strs:
            zeros, ones = 0, 0
            for ch in str:
                if ch == '0':
                    zeros +=1
                else:
                    ones += 1
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    DP[i][j] = max(DP[i][j], DP[i - zeros][j-ones]+1)
        return DP[-1][-1]

        
# @lc code=end

