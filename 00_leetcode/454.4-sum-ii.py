#
# @lc app=leetcode id=454 lang=python
#
# [454] 4Sum II
#

# @lc code=start
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #two hashtable
        #2 2-sums
        h = collections.defaultdict(int)
        for a in A:
            for b in B:
                h[a+b]+=1
        cnt = 0
        for c in C:
            for d in D:
                if -c-d in h:
                    cnt+=h[-c-d]
        return cnt
        
# @lc code=end

