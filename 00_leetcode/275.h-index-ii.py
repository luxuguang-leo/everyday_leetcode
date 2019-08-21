#
# @lc app=leetcode id=275 lang=python
#
# [275] H-Index II
#
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        start, end = 0, l-1
        h = 0
        while start <= end:
            mid = start + (end - start)//2
            h = max(h, min(citations[mid], l - mid))
            if citations[mid] > l - mid:
                end = mid -1
            else:
                start = mid + 1
        return h
        

