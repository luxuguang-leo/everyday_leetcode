#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def dfs(self, remain_left, remain_right, ret, path):
        if remain_left == 0 and remain_right == 0:
            ret.append(path)
            return
        #if remain_left > 0 and remain_left >= remain_right:
        #Add left parenthesis if possible
        #这里有两条选择路径1.如果左边括弧还有剩余，可以直接添加
        #2.如果右边括弧数目大于左边括弧，那么添加有括弧是安全的，添加有括弧
        if remain_left > 0:
            self.dfs(remain_left-1, remain_right, ret, path+'(')
        if remain_right > 0 and remain_right > remain_left:
            self.dfs(remain_left, remain_right-1, ret, path+')')

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        if n <= 0:
            return []
        ans = []
        self.dfs(n, n, "", ans)
        return ans
        '''
        '''
        if n == 0:
            return []
        ret = []
        self.dfs(n, n, ret, "")
        return ret
        '''
        #another way is to insert pair of parentheses in (n-1)
        if n == 0:
            return []
        #ans保存的是上一次n-1能形成的结果列表
        #n==2, ans = ["(())", "()()"]
        ans = ["()"]
        for i in range(1, n):
            tmp = []
            for x in ans:
                for y in range(len(x)):
                    tmp.append(x[:y]+"()"+x[y:])
            ans = list(set(tmp))
        return ans



