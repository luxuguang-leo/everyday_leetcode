#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
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
        l, r = 0, m*n-1
        while l <= r:
            mid = l + (r-l)//2
            if target == matrix[mid/n][mid%n]:
                return True
            elif target < matrix[mid/n][mid%n]:
                r = mid -1
            else:
                l = mid +1
        return False
        
# @lc code=end

