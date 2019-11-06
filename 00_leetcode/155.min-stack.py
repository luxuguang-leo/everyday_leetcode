#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.q_min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        if not self.q_min or x <= self.q_min[-1]:
            self.q_min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        n = self.q.pop()
        if n <= self.q_min[-1]:
            self.q_min.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.q_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

