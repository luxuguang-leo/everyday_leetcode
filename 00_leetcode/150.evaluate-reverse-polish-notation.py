#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.operators = {
            '+':lambda y, x: x+y,
            '-':lambda y, x: x-y,
            '*':lambda y, x: x*y,
            '/':lambda y, x: int(operator.truediv(x, y))
        }
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []

        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0] 
# @lc code=end

