#
# @lc app=leetcode id=547 lang=python
#
# [547] Friend Circles
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            for neigh, val in enumerate(M[i]):
                if val and neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)
        N = len(M)
        seen = set()
        cnt = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                cnt+=1
        return cnt
            
# @lc code=end

