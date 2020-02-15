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
        #method 1,插入之后按照56来做,注意插入尾部的情况，这里先让idx为最后一个值，避免了最后一个节点
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
        '''
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
        '''
        #由于是有序数组，可以使用二分查找来降低时间复杂度，核心在于找到左半部分，右半部分
        #通过寻找插入的位置来扩展合并单元
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        l = len(intervals)
        low = bisect.bisect_left([i[1] for i in intervals], newInterval[0])
        high = bisect.bisect_right([i[0] for i in intervals], newInterval[1])
        #1.这里寻找左边界的时候为何前面数组用的每一个区间的右半段呢？因为如果使用做半段，得出的位置并不是真实要插入的位置，有可能前面一个区间的尾部大于这个左边界
        #所以使用右边边界作为二分数组，找到插入的位置，这个位置可以准确判断要插入的区间，
        #但是左边的边界还要继续根据newInterval的左边界和之前这个区间的左边界来确定
        if low < l:
            newInterval[0] = min(newInterval[0], intervals[low][0])
        #2.寻找右边界一样的道理，要准确找到右边要插入的区间索引，需要用newInterval右边界和所有左区间的来二分
        #找到位置之后需要确定右边界，还需要newInterval右边界和要插入的区间的右边界来继续确认
        if high > 0:
            newInterval[1] = max(newInterval[1], intervals[high-1][1])
        return intervals[:low] + [newInterval] + intervals[high:]



        

        
# @lc code=end

