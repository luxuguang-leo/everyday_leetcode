#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

class Intervals(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        ret = []
        intervals.sort(key = lambda x: x.start)
        ret.append(Intevals(intervals[0])
        for n in intervals:
            pre = ret[-1]
            if n.start <= pre.end:
                pre.end = max(pre.end, n.end)
            else:
                ret.append(n)
        return ret


