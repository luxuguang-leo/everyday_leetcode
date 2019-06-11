#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (36.20%)
# Total Accepted:    285.7K
# Total Submissions: 785.3K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_1.append(x)
        if len(self.stack_2) == 0 or x <= self.stack_2[-1]:
            self.stack_2.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack_1[-1]
        self.stack_1.pop()
        if val == self.stack_2[-1]:
            self.stack_2.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack_1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

