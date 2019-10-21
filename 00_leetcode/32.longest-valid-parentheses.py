#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #method 1, use stack
        '''
        left_most, max_len = -1, 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                    if len(stack) != 0:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - left_most)
                else:
                    left_most = i
        return max_len
        '''
        #we can initialize the stack with -1 first
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len

        #method DP?

        

