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
        self.stack = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        l = len(self.stack)
        self.stack.append(x)
        for _ in range(l):
            self.stack.append(self.stack.popleft())
        print("push", self.stack)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.stack.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

