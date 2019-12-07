#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        #method 1,插入之后按照56来做
        '''
        idx = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                idx = i
                break
        intervals.insert(idx, newInterval)
        ret = []
        ret.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ret[-1][1]:
                ret[-1][-1] = max(ret[-1][-1], intervals[i][1])
            else:
                ret.append(intervals[i])
        return ret
        '''

        #method 2, l + interleave + r, 重叠区域的边界s,e都是动态改变的
        s, e = newInterval[0], newInterval[1]
        l,r = [],[]
        for interval in intervals:
            if interval[1] < s:
                l.append(interval)
            elif interval[0] > e:
                r.append(interval)
            else:
                s = min(s, interval[0])
                e = max(e, interval[1])
        return l + [[s,e]]+r

        

        
# @lc code=end

