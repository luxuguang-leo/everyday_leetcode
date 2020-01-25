#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def dfs(self, left_remain, right_remain, path, ret):
        if left_remain == 0 and right_remain == 0:
            ret.append(path)
        if left_remain > 0:
            self.dfs(left_remain-1, right_remain, path+'(', ret)
        if right_remain > left_remain:
            self.dfs(left_remain, right_remain-1, path + ')', ret)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ret = []
        self.dfs(n, n, '', ret)
        return ret
        

