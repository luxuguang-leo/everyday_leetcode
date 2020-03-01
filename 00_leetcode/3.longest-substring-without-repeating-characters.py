#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #sliding window, record the position of each char
        '''
        start = 0
        ans = 0
        m = {}
        for i in range(len(s)):
            if s[i] in m and start <= m[s[i]]:
                start = m[s[i]] + 1
            else:
                ans = max(ans, i - start + 1) 
            m[s[i]] = i
        return ans
        '''
        #更新start的条件就是出现的字符串已经超过start,这时再以start为起点的字符串肯定包含重复字符，所以需要更
        #@0301,
        #1.每一次字符都要更新map表，都要求当前的最大窗口长度
        #2.当碰到重复字符的时候，可能需要更新窗口的左边界，但是如果重复的字符不在滑动窗口内，不需要更新的，例如:
        #mabcdfm
        #如果当前左窗口是b，到最右边的m时候，发现m已经重复过，但是并不在滑动窗口内，所以不需要更新，更新会损失m和左边界的一部分宽度
        if not s:
            return 0
        m = {}
        ans, start = 0, 0
        for i in range(len(s)):
            if s[i] in m and start <= m[s[i]]:
                start = m[s[i]] + 1
            else:
                ans = max(ans, i - start +1)
            m[s[i]] = i
        return ans


        
# @lc code=end

