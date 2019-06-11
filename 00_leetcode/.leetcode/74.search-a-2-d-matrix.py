#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #extend all arrays into 1-dimension array
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = l + (r-l)//2
            val = matrix[mid/n][mid%n]
            if val == target:
                return True
            elif val < target:
                l = mid +1
            else:
                r = mid -1
        return False
        

