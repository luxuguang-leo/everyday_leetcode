#
# @lc app=leetcode id=395 lang=python
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #学习网上一个devide-conquer解法
        #1.遍历s,用一个map记录字符出现的次数，=
        #2.判断整体是否满足，如果满足则返回字符串长度？这个的目的是用来递归的边界
        #3.如果发现某一个字符的次数小于k，则用这个字符将原始长字符切割成两端
        #4.对每一段递归调用得出最终解,python太优美了，短短6行就解决问题！
        '''
        if not s or len(s) < k:
            return 0
        for c in set(s):#剔除重复数目
            if s.count(c) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return (len(s))
        '''
        #method, sliding windows?没想清楚左面指针如何移动，因为如果只遍历一次的话如果左面指针小于k并不能马上更新滑动窗口
        #1.扫描一次s,得出字符和次数的map
        #2.初始化左右窗口，往右滑动窗口
        #3.如果字符在最终的map结果中小于k，那么计算之前的窗口，并且windows更新到
        if len(s) < k:
            return 0
        m = collections.Counter(s)
        l = ret = 0
        hash_s = {}
        for i in range(len(s)):
            #hash_s
            if m[s[i]] < k:
                ret = max(ret, i - l)
                l = i +1
            else:
                ret = max(ret, i-l)
        return ret

        
# @lc code=end

