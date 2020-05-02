#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
class Solution(object):
    def helper(self, s, l, r):
        #注意区间边界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;r += 1
        return s[l+1:r] #起始位置应该是l+1,由于是开区间，右边界应该是r

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #method 1, brute force, O(N^2)
        '''
        if len(s) <= 1:
            return s
        ret = ""
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(ret):
                ret = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(ret):
                ret = tmp
        return ret
        '''
        #马拉车算法, O(N)
        #1.插入dummy字符，转换成奇数长的字符串
        #2.DP算法求RL[i]
        #3.根据max_right和RL[i]找出字符串的位置
        #参考--https://blog.csdn.net/dyx404514/article/details/42061017
        #参考--https://segmentfault.com/a/1190000003914228
        if len(s) <= 1:
            return s
        T = '#' + '#'.join(s) + '#'
        RL = [0]*len(T)
        index = 0
        max_right = 0
        ret = ""
        max_len = 0
        for i in range(len(T)):
            if i < max_right:
                RL[i] = min(RL[2*index - i], max_right - i) 
            else:
                RL[i] = 1
            while i >= RL[i] and i + RL[i] < len(T) and T[i + RL[i]] == T[i - RL[i]]:
                RL[i] += 1
            if i + RL[i] - 1 > max_right:
                max_right = i + RL[i] -1
                index = i
            if RL[i] > max_len:
                max_len = RL[i]
                ret = s[(i+1-max_len)//2:(i-1+max_len)//2]
        return ret




