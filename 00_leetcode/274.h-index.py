#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0 
        citations.sort()
        for i in range(len(citations)):
            h = max(h, min(len(citations)-i, citations[i]))
        return h
        

