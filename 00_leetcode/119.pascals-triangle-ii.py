#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prelist = [1,1]
        for i in range(2, rowIndex+1):
            path = [1]*(rowIndex+1)
            for n in range(1,i):
                path[n] = prelist[n] + prelist[n-1]
            del prelist[:]
            prelist = path[:]
        return prelist
# @lc code=end

