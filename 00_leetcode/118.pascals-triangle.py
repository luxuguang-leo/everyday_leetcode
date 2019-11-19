#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows ==1:
            return [[1]]
        if numRows ==2:
            return [[1],[1,1]]
        ret = [[1], [1,1]]
        for row in range(2, numRows):
            path = [1]*(row+1)
            ret.append(path)
            print(ret)
            for i in range(1,row):
                ret[row][i] = ret[row-1][i] + ret[row-1][i-1]
        return ret

        
# @lc code=end

