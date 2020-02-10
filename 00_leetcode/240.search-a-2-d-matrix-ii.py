#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        #从右上角来进行搜索，小于则向左搜索，大于则向下搜索
        x, y = 0, n-1
        while y >=0 and x < m:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                x +=1
            else:
                y-=1
        return False
        
# @lc code=end

