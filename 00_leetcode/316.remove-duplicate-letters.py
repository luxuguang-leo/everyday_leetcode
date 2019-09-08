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
        #遍历串，得到所有的次数
        #维持一个stack，遍历字串规则：
        #如果字符不在stack中，如果发现栈顶元素数目大于1（后面还有这个元素）&& 此元素大于字符，那么需要将栈顶元素出栈，
        #直到 栈空 栈顶元素小于字符 或者 字符只出现一次
        if not s:
            return ""
        cnt = {}
        for ch in s:
            cnt.setdefault(ch,0)
            cnt[ch] +=1
        stack = []
        for c in s:
            if c not in stack:
                while stack and cnt[stack[-1]] > 1 and stack[-1] >= c:
                    cnt[stack[-1]] -= 1
                    stack.pop()
                stack.append(c)
            else:
                cnt[c] -= 1
        return ''.join(stack)


        

