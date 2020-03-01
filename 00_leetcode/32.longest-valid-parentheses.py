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
        '''
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
        '''
        '''
        if not s:
            return 0
        max_len, left = 0, -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - left)
                else:
                    left = i
        return max_len
        '''
        '''
        if not s:
            return 0
        max_len, stack = 0, [-1]#初始化stack -1避免了在栈为空的情况下的来两种情况只需要判断一次即可
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len
        '''

        #method DP
        #非常难想，我觉得是hard级别的
        #例如"( ) ( ( ) )",如果DP[i]代表包含s[i]的最长配对长度，那么有以下几种情况：
        #1.如果s[i] == '(', DP[i]为0
        #2.如果s[i] == ')',有一下几种情况，
        ## 2.a如果前一个s[i-1]为'('，那么DP[i] = DP[i-2]+2
        ## 2.b如果前一个s[i-1]为')',那么首先看之前还有多少剩下的左括弧，如果有，那么至少
        ### DP[i] = DP[i-1]+2，然后看DP[i-DP[i]]是否还有值，如果有值应该加上DP[i-DP[i]]
        ### 所以递推公式应该是DP[i] = DP[i-1] + 2
        #DP += DP[i-DP[i]]
        #DP分为两部分，DP[i-1]部分和DP[i-DP[i]]部分
        '''
        if not s:
            return 0
        leftCount, ret = 0, 0
        DP = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                leftCount +=1
            elif leftCount > 0:
                DP[i] = DP[i-1] + 2
                #print(s[i], DP, leftCount)
                if i - DP[i] >= 0:#证明索引i-DP[i]之前有连续的括弧对，要加上
                    DP[i] += DP[i-DP[i]]
                leftCount -=1
            ret = max(ret, DP[i])#如果
        return ret
        '''
        #@0301,使用stack,初始化-1
        #有两种特殊情况需要考虑：
        # 1.（）这种，当有括弧的时候，弹出栈，栈为空，但是需要求出win大小，这时候可以初始化一个-1避免这种情况
        # 2. )()这种，当碰到第一个右边括弧的时候，弹出栈，发现栈空了，这时候该如何处理呢？需要将当前元素push进去
        #       否则后面需要求窗口大小的时候没办法求
        if not s:
            return 0
        stack, max_win = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_win = max(max_win, i - stack[-1])
                    else:
                        stack.append(i)
        return max_win




        

