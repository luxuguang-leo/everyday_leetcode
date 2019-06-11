#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """






        m, n = len(matrix) -1, len(matrix[0]) -1
        for i in range(m):
            for j in range(n, -1, -1):
                if matrix[i][j] == target:
                    return True
                if matrix[i]


        

