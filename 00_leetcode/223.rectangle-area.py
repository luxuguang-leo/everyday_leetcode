#
# @lc app=leetcode id=223 lang=python
#
# [223] Rectangle Area
#

# @lc code=start
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #如果有交集才需要处理，无交集不需要减去重叠部分面积
        # method 1
        '''
        S = (C-A)*(D-B) + (G-E)*(H-F)
        x1, y1, x2, y2 = max(A, E), max(B, F), min(C, G), min(D, H)
        if x1 < x2 and y1 < y2:
            S -= (x2-x1)*(y2-y1)
        return S
        '''
        return (C-A)*(D-B)+(G-E)*(H-F) - max(0, min(G,C) - max(E,A))*max(0, min(D, H)-max(B,F))
        
# @lc code=end

