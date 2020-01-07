#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        t_map = collections.Counter(t)
        wanted = len(t)
        l, cnt = 0, 0
        res = ""
        min_len = len(s) + 1
        for r in range(len(s)):
            if s[r] in t_map:
                t_map[s[r]] -=1
                if t_map[s[r]] >=0:
                    cnt +=1
                while cnt == wanted:#到达区间右边界，需要尝试更新区间左边界
                    #如果发现此时的窗口更小，则更新串口长度
                    if r - l + 1 < min_len:
                        min_len = r - l +1
                        res = s[l:r+1]
                    #继续往右收缩左窗口，如果发现在map中，则将map增加，cnt减少，打破平衡导致
                    #右窗口往右滑动
                    if s[l] in t_map:
                        t_map[s[l]] +=1
                        if t_map[s[l]] > 0:
                            cnt -=1
                    l +=1
        return res 

       