#
# @lc app=leetcode id=316 lang=python
#
# [316] Remove Duplicate Letters
#
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        #使用一个map来统计
        #然后维持一个单调递增的栈
        #1.如果当前元素在栈中，则计数减一，why?因为栈本身就是有序字符，无需更新
        #2.如果当前元素不在栈中
        #   2.1 如果栈顶元素比较大，且栈顶元素比较大，那么弹出栈，且计数-1，压入当前元素
        #   2.2 如果栈顶元素比较小，压入栈即可
        #3.最终将栈拼接，即可得到一个有序字符串
        if not s:
            return ""
        stack = []
        cnt = collections.Counter(s)
        for ch in s:
            if ch not in stack:
                while stack and ch <= stack[-1] and cnt[stack[-1]] > 1:
                    cnt[stack.pop()] -=1
                stack.append(ch)
            else:
                cnt[ch] -=1
        return "".join(stack)
        '''
        #遍历stack带来的代价是O(n)时间复杂度，我们可以用空间换时间，用一个bool型set来记录有无访问过
        #在以上基础上，如果栈顶元素出栈，则标记此元素为false
        #如果append,则标记为True
        if not s:
            return ""
        stack = []
        cnt = collections.Counter(s)
        visited = collections.defaultdict(bool)
        for ch in s:
            cnt[ch] -=1
            if visited[ch]:
                continue
            while stack and ch < stack[-1] and cnt[stack[-1]]:
                visited[stack.pop()] = False
            stack.append(ch)
            visited[ch] = True
        return "".join(stack)
            


        

