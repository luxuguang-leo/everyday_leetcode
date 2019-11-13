#
# @lc app=leetcode id=89 lang=python
#
# [89] Gray Code
#

# @lc code=start
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return ['0']
        if n == 1:
            return ['0','1']
        prelist = ['0', '1']
        for i in range(2, n+1):
            tmp = []
            for s in prelist:
                tmp.append('0'+s)
            for s in prelist[::-1]:
                tmp.append('1'+s)
            prelist = tmp
        return map(lambda x: int(x, 2), prelist)
        
# @lc code=end

