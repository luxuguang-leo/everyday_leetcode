#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q_in, self.q_out = [], []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.q_in.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.q_out) == 0:
            while len(self.q_in) != 0:
                self.q_out.append(self.q_in.pop())
        return self.q_out.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.q_out) == 0:
            while len(self.q_in) != 0:
                self.q_out.append(self.q_in.pop())
        return self.q_out[-1]

        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.q_in) == 0 and len(self.q_out) == 0:
            return True
        else:
            return False
        #return len(self.q_in) !=0 and len(self.q_out) != 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

