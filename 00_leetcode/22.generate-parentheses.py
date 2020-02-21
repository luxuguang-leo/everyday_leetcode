#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def dfs(self, left_remain, right_remain, path, ret):
        if left_remain == 0 and right_remain == 0:
            ret.append(path)
            return ret
        if left_remain >0:
            self.dfs(left_remain-1, right_remain, path+'(', ret)
        if right_remain > left_remain:
            self.dfs(left_remain, right_remain-1, path+')', ret)
        
   

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #method, using backtracking
        '''
        ret = []
        self.dfs(n, n, '', ret)
        return ret
        '''
        #通过N-1推N，在每一个可能的N-1字符结果中插入'()'，去除重复
        if n == 0:
            return ['']
        ans = ['()']
        for _ in range(1, n):
            tmp = []
            for x in ans:
                for j in range(len(x)):
                    tmp.append(x[:j] + '()'+ x[j:])
            ans = list(set(tmp))
        return ans



        

