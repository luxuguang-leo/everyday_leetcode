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
        '''
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
        '''

        #@0229, 使用右上角的数字作为首先的数组，根据规律进行提出操作，O(M+N)
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1
        while c >= 0 and r <= m-1:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -=1
            else:
                r+=1
        return False
        
# @lc code=end

