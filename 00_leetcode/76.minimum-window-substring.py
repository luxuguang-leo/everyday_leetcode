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
        dict_t = collections.Counter(t)
        wanted = len(t)
        l , r = len(s), 2*len(s)
        deq = collections.deque([])
        d = {}
        score = 0
        for i, c in enumerate(s):
            if c in dict_t:
                deq.append(i)
                d[c] = d.get(c, 0) +1
                if d[c] <= dict_t[c]:
                    score +=1
                while deq and d[s[deq[0]]] > dict_t[s[deq[0]]]:
                    d[s[deq.popleft()]] -=1
                if score == wanted and deq[-1] - deq[0] < r - l:
                    l , r = deq[0], deq[-1]
        return s[l:r+1]
       