#
# @lc app=leetcode id=385 lang=python
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        '''
        def nestedInteger():
            num = ''
            while s[-1] in '1234567890-':
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(nestedInteger())
                if s[-1] == ',':
                 s.pop()
            s.pop()
            return lst
        s = list(' ' + s[::-1])
        return nestedInteger()
        '''
        cur = None
        stack, num, sign = [], 0, 1
        for c in s:
            if c.isdigit():
                if cur == None:
                    cur = NestedInteger(0)
                cur.setInteger(cur.getInteger() * 10 + int(c) * sign)
            elif c == ',':
                stack[-1].add(cur)
                cur = None
                sign = 1
            elif c == '[':
                cur = NestedInteger([])
                stack.append(cur)
                cur = None
            elif c == ']':
                if cur != None:
                    stack[-1].add(cur)
                cur = stack.pop()
            elif c == '-':
                sign = -1
        
        return cur



# @lc code=end

