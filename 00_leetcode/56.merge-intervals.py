#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sort,然后依次比较前一个pair和后一个pair
        #1.有重合，并且后一个尾比较长，则更新交集区间为前pair的头和后pair的尾
        #2.有重合，但前一个尾比较长，则前一个保持
        #3.无重合， 将后一个pair入结果
        if len(intervals) <= 1:
            return intervals
        ret = []
        intervals.sort()
        ret.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ret[-1][1]:
                ret[-1][-1] = max(ret[-1][-1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret
        
# @lc code=end

