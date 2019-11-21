#
# @lc app=leetcode id=225 lang=python
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        l = len(self.s1)
        self.s1.append(x)
        while l > 0:
            self.s1.append(self.s1.popleft())
            l -= 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.s1.popleft()
        


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.s1[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.s1) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

