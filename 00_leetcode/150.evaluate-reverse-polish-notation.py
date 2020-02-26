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
        '''
        if not tokens:
            return 0
        stack = []

        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0] 
        '''
        #don't use lambda expression
        if not tokens:
            return 0
        stack = []
        for item in tokens:
            if item not in ('+', '-', '*', '/'):
                stack.append(item)
            else:
                left, right = stack.pop(), stack.pop()
                if item == '/':
                    value = int(float(right)/float(left))
                else:
                    value = eval(right+item+left)
                stack.append(str(value))
        return int(stack[0])

# @lc code=end

