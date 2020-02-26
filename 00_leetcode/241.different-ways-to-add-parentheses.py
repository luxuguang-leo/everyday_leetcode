#
# @lc app=leetcode id=241 lang=python
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.cach = collections.defaultdict(list)

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        #method 1, devide-and-conqure
        '''
        if input.isdigit():
            return [int(input)]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        ret.append(eval(str(l) + c + str(r)))
        return ret
        '''
        #method 2, use memory for speedup,如何改成DP？
        #这个思维的难点在于递归返回的是一个表达式的可能的所有值，所以在Divide之后，对左半部分的结果应该是取其中一个
        #再分别取右半部分的list中的一个，分别计算，然后组合得出结果，最终返回的是整个结果list
        if input.isdigit():
            return [int(input)]
        if input in self.cach:
            return self.cach[input]
        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        ret.append(eval(str(l) + c + str(r)))
        self.cach[input] = ret
        return ret



# @lc code=end

