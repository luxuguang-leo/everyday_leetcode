#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def dfs(self, left, right, path, ret):
        if left > 0:
            self.dfs(left-1, right, path+'(', ret)
        if right > 0 and right > left:
            self.dfs(left, right-1, path + ')', ret)
        if left == 0 and right == 0:
            ret.append(path)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ret = []
        self.dfs(n, n, '', ret)
        return ret
        

