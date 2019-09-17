#
# @lc app=leetcode id=214 lang=python
#
# [214] Shortest Palindrome
#
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #manache algo
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index, max_right = 0, 0
        T = '$' + '$'.join(s) + '$'
        L = len(T)
        RL = [0]*L
        max_len = 0
        for i in range(L):
            if i < max_right:
                RL[i] = min(RL[2*index-i], max_right - i)
            else:
                RL[i] = 1
            while i >= RL[i] and i + RL[i] < L and T[i-RL[i]] == T[i+RL[i]]:
                RL[i] += 1
            if i + RL[i] - 1 > max_right:
                max_right = i + RL[i] - 1
                index = i
            if RL[i] > max_len and i+1 == RL[i]:
                max_len = RL[i]
        #print index, max_len, len(s)
        print s[len(s)-1:max_len-2:-1]
        return s[len(s)-1:max_len-2:-1]+ s
            
        

